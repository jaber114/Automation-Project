import os
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.safari.options import Options
from selenium.webdriver.edge.options import Options
from Utils.config import ConfigReader

# Fixture that sets up the webdriver and opens the browser
@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global driver
    options = Options()
    # Keeps browser open after test completion
    options.add_experimental_option("detach",True)
    # Determines which browser to use
    browser_type=browsertype()
    match browser_type:
        case "Chrome":
         driver = webdriver.Chrome(options=options)
        case "Firefox":
         driver = webdriver.Firefox(options=options)
        case "Edge":
         driver = webdriver.Edge(options=options)
        case "Safari":
         driver = webdriver.Safari(options=options)
    # Assigns the driver to the test class
    request.cls.driver = driver
    # Maximizes the browser window
    driver.maximize_window()
    # Reads the URL from the config file
    url=ConfigReader.read_config("general","url")
    # Opens the URL in the browser
    driver.get(url)
    yield
    # Closes the browser after the test
    driver.quit()
# Hook that runs after the test session finishes and writes environment details to a file
def pytest_sessionfinish() -> None:
    browser_type=browsertype()
    environment_properties = {
     'browser': browser_type,
     'driver_version': driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)
# Hook that takes a screenshot when a test fails,SC can be viewed in the allure reports
def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

# Helper function that reads the browser type from the configuration file
def browsertype():
    Browser=ConfigReader.read_config("browser","browser_type")
    match Browser:
     case "Chrome":
          return "Chrome"
     case "Firefox":
         return "Firefox"
     case "Edge":
         return "Edge"
     case "Opera":
         return "Opera"
     case "Safari":
         return "Safari"