from selenium.webdriver.common.by import By

from Pages.Basepage import BasePage


class Checkoutforms(BasePage):
    Check_out_button = (By.CSS_SELECTOR,"#content > div.buttons.clearfix > div.pull-right > a")
    Order_success_message = (By.CSS_SELECTOR,"#content > h1")
    Payment_method_text_area = (By.CSS_SELECTOR,"#collapse-payment-method > div > p:nth-child(4) > textarea")
    Terms_and_conditions_checkbox = (By.CSS_SELECTOR,"#collapse-payment-method > div > div.buttons > div > input[type=checkbox]:nth-child(2)")
    delivery_method_text_area = (By.CSS_SELECTOR,"#collapse-shipping-method > div > p:nth-child(5) > textarea")
    Continue_button = (By.CSS_SELECTOR,"#button-payment-address")
    Payment_error_message = (By.CSS_SELECTOR,"#collapse-payment-method > div > div.alert.alert-danger.alert-dismissible")
    Address_select_options = (By.CSS_SELECTOR,"#payment-existing > select")
    Confirm_order_btn = (By.CSS_SELECTOR,"#button-confirm")
    # Contact us page
    Validation_text = (By.CSS_SELECTOR,"#content > h1")
    Contact_us_button = (By.CSS_SELECTOR,"body > footer > div > div > div:nth-child(2) > ul > li:nth-child(1) > a")
    Name=(By.CSS_SELECTOR,"#input-name")
    Email_Address=(By.CSS_SELECTOR,"#input-email")
    Enquiry=(By.CSS_SELECTOR,"#input-enquiry")
    Submit_button=(By.CSS_SELECTOR,"#content > form > div > div > input")
    Delivery_details_selection = (By.CSS_SELECTOR,"#shipping-existing > select")
    Delivery_details_continue_button = (By.CSS_SELECTOR,"#button-shipping-address")
    Delivery_method_contine_button = (By.CSS_SELECTOR,"#button-shipping-method")
    Payment_Continue_button = (By.CSS_SELECTOR,"#button-payment-method")
    Submit_form_button = (By.CSS_SELECTOR,"#content > form > div > div > input")
    def __init__(self,driver):
        super().__init__(driver)




    def billing_details(self,option):
        self.delay(3)
        self.bill_details(self.Address_select_options,self.Continue_button,option)

    def delivery_details(self,details):
        self.delay(3)
        self.delivery_dtls(self.Delivery_details_selection,self.Delivery_details_continue_button,details)





    def delivery_method(self,text):
        self.delay(4)
        self.delivery_mth(self.delivery_method_text_area,text,self.Delivery_method_contine_button)


    def Payment_method(self,text):
        self.delay(3)
        self.pay_method(self.Payment_method_text_area,self.Terms_and_conditions_checkbox,text,self.Payment_Continue_button)

    def payment_validation(self):
        self.delay(2)
        return self.pay_validation(self.Payment_error_message)

    def confirm_order(self):
        self.delay(3)
        self.order_confirm(self.Confirm_order_btn)

    def Contact_us_form(self,name,Email,Enquiry):
        self.delay(2)
        self.Contact_us(
        self.Name,
        self.Email_Address,
        self.Enquiry,
        name,
        Email,
        Enquiry,
        self.Submit_button
        )

    def contact_form_validation(self):
        self.delay(4)
        return self.form_validation(self.Validation_text)


    def checkout(self):
        self.delay(3)
        self.chck_out(self.Check_out_button)


    def confirm_order_validation(self):
        self.delay(3)
        self.confirm_validation(self.Order_success_message)

    def contact_us_page(self):
        self.contact_page(self.Contact_us_button)


    def submit(self):
        self.delay(2)
        self.submit_button(self.Submit_form_button)





