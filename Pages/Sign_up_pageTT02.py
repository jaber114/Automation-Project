from selenium.webdriver.common.by import By

from Pages.Basepage import BasePage
from Utils.config import ConfigReader


class signup(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
    menubutton = (By.CSS_SELECTOR,"#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
    Sign_up_button = (By.CSS_SELECTOR,"#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
    First_name = (By.CSS_SELECTOR,"#input-firstname")
    Last_name =  (By.CSS_SELECTOR,"#input-lastname")
    Email = (By.CSS_SELECTOR,"#input-email")
    Telephone = (By.CSS_SELECTOR,"#input-telephone")
    Password = (By.CSS_SELECTOR,"#input-password")
    Password_confirm = (By.CSS_SELECTOR,"#input-confirm")
    Privacy_policy_btn = (By.CSS_SELECTOR,"#content > form > div > div > input[type=checkbox]:nth-child(2)")
    Signup_message = (By.CSS_SELECTOR,"#content > h1")
    continue_btn=(By.CSS_SELECTOR,"#content > form > div > div > input.btn.btn-primary")
    def visit_signuppage(self):
        self.signup_page(self.Sign_up_button)

    def menu_button(self):
        self.Menu(self.menubutton)

    def Fill_signup(self,
    first_name_value,
    last_name_value,
    Email_value,
    Telephone_value,
    Password_value,
    Confirm_pass):
       self.delay(5)
       self.fill_signup_form(
        first_name_value,
        self.First_name,
        last_name_value,
        self.Last_name,
        Email_value,
        self.Email,
        Telephone_value,
        self.Telephone,
        Password_value,
        self.Password,
        Confirm_pass,
        self.Password_confirm
       )


    def current_url(self):
        return self.get_url()
    def wait(self,milli_seconds):
        self.delay(milli_seconds)

    def success_message(self):
        self.signup_message(self.Signup_message)

    def confirm_password(self):
        return self.pass_confirm(self.Password,self.Password_confirm)

    def privacy_check(self):
        self.check(self.Privacy_policy_btn)

    def Register(self):
        self.register(self.continue_btn)






