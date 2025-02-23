from selenium.webdriver.common.by import By

from Pages.Basepage import BasePage


class user_actions(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    password_field=(By.CSS_SELECTOR,"#input-password")
    password_confirm=(By.CSS_SELECTOR,"#input-confirm")
    My_account_page_button = (By.CSS_SELECTOR,"#top-links > ul > li.dropdown > a")
    Change_passwod_page_button = (By.CSS_SELECTOR,"#content > ul:nth-child(2) > li:nth-child(2) > a")
    password_charsvalidtext = (By.CSS_SELECTOR,"#content > form > fieldset > div.form-group.required.has-error > div > div")
    Password_notmatch = (By.CSS_SELECTOR,"#content > form > fieldset > div.form-group.required.has-error > div > div")
    Continue_button = (By.CSS_SELECTOR,"#content > form > div > div.pull-right > input")
    first_name_field = (By.CSS_SELECTOR,"#input-firstname")
    Last_name_field = (By.CSS_SELECTOR,"#input-lastname")
    Email_field = (By.CSS_SELECTOR,"#input-email")
    Phone_field = (By.CSS_SELECTOR,"#input-telephone")
    Input_fields_update_info= (By.CSS_SELECTOR,".col-sm-10>div")
    Edit_account_info_button = (By.CSS_SELECTOR,"#content > ul:nth-child(2) > li:nth-child(1) > a")
    Subscribe_page_button = (By.CSS_SELECTOR,"#content > ul:nth-child(8) > li > a")
    Subscribe_action_button = (By.CSS_SELECTOR,"#content > form > fieldset > div > div > label:nth-child(1) > input[type=radio]")
    Unsubscribe_action_button = (By.CSS_SELECTOR,"#content > form > fieldset > div > div > label:nth-child(2) > input[type=radio]")
    Subscription_message =(By.CSS_SELECTOR,"#account-account > div.alert.alert-success.alert-dismissible")
    # Address Book Entries
    address_first_name=(By.CSS_SELECTOR,"#input-firstname")
    address_last_name = (By.CSS_SELECTOR,"#input-lastname")
    Address1 = (By.CSS_SELECTOR,"#input-address-1")
    City=(By.CSS_SELECTOR,"#input-city")
    Post_code= (By.CSS_SELECTOR,"#input-postcode")
    Country=(By.CSS_SELECTOR,"#input-country")
    Region_field = (By.CSS_SELECTOR,"#input-zone")
    New_address_button = (By.CSS_SELECTOR,"#content > div.buttons.clearfix > div.pull-right > a")
    Modify_address_book = (By.CSS_SELECTOR,"#content > ul:nth-child(2) > li:nth-child(3) > a")
    Modify_book_success_message=(By.CSS_SELECTOR,"#account-address > div.alert.alert-success.alert-dismissible")
    def change_password(self,password):
        self.delay(3)
        self.change_pass(
        self.password_field,
        self.password_confirm,
        self.Continue_button,
        password
        )
    def myaccount_page(self):
        self.delay(3)
        self.navigate_to_myacc_page(self.My_account_page_button)
    def chanepass_page(self):
        self.delay(3)
        self.navigate_to_myacc_page(self.Change_passwod_page_button)

    def changepass_validaiton(self):
        self.delay(3)
        return self.changepassvalidation(self.password_charsvalidtext,self.Password_notmatch)
    def change_user_information(self,first_name,last_name,Email,Phone):
        self.delay(4)
        self.update_user_info(
        self.first_name_field,
        self.Last_name_field,
        self.Email_field,
        self.Phone_field,
        first_name,
        last_name,
        Email,
        Phone,
        self.Continue_button
        )

    def update_info_validation(self):
        self.delay(3)
        return self.info_validation(self.Input_fields_update_info)

    def Edit_info_page(self):
        self.delay(3)
        self.edit_page(self.Edit_account_info_button)


    def Newsletter_page(self):
        self.delay(3)
        self.newsletter_screen(self.Subscribe_page_button)

    def subscribe_to_newsletter(self):
        self.delay(4)
        self.subscribe(self.Subscribe_action_button,self.Continue_button)

    def unsubscribe_to_newsletter(self):
        self.delay(3)
        self.unsubscribe(self.Unsubscribe_action_button,self.Continue_button)
    def validate_subscription(self):
        self.delay(2)
        return self.subscription_validation(self.Subscription_message)
    def add_Address_Book_Entries(self,
    first_name,
    last_name,
    address1,
    city,
    post_code,
    country,
    Region,
            ):
        self.add_address_book(
        self.address_first_name,
        self.address_last_name,
        self.Address1,
        self.City,
        self.Post_code,
        self.Country,
        self.Region_field,
        first_name,
        last_name,
        address1,
        city,
        post_code,
        country,
        Region,
        self.Continue_button

        )
    def modify_address_book(self):
        self.delay(3)
        self.Modify_add_book(self.Modify_address_book)

    def New_address_book(self):
        self.delay(2)
        self.New_address(self.New_address_button)

    def address_book_entries_validation(self):
        return self.address_bookvalidation(self.Modify_book_success_message)








