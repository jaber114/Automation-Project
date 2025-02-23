import allure
from selenium.webdriver.common.by import By
import time
from Pages.Basepage import BasePage
import pytest

class login(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    menubutton = (By.CSS_SELECTOR,"#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
    menuLogin_button = (By.CSS_SELECTOR,"#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a")
    Logout_button = (By.CSS_SELECTOR,"#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a")
    Email_field = (By.CSS_SELECTOR,"#input-email")
    Password_field = (By.CSS_SELECTOR,"#input-password")
    Login_btn = (By.CSS_SELECTOR,"#content > div > div:nth-child(2) > div > form > input")
    Error_msg=(By.CSS_SELECTOR,"#account-login > div.alert.alert-danger.alert-dismissible > i")
    def wait(self,milli_seconds):
        self.delay(milli_seconds)
    def menu_button(self):
        self.Menu(self.menubutton)
    def login_L01(self):
        self.login_step(self.menuLogin_button)
    @allure.step("login with username: {username} and password : {password}")
    def fill_info(self,username,password):
        self.fill_login_form(
        self.Email_field,
        self.Password_field,
        username,
        password
        )
        self.delay(3)

    def current_url(self):
        return self.get_url()
    def loginbtn(self):
        self.logbtn(self.Login_btn)

    def logout(self):
        self.Menu(self.menubutton)
        self.delay(4)
        self.sign_out(self.Logout_button)

    def Error_msg(self):
        return self.errmsg(self.Error_msg)
