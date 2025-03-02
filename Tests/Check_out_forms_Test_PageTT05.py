from collections.abc import Mapping
from subprocess import check_output

import allure
import pytest
from allure_commons.types import Severity
from allure_pytest.utils import allure_description, allure_title

from Pages.Check_out_forms_PageTT05 import Checkoutforms
from Pages.Choose_product_PageTT04 import Choose_product
from Pages.Login_pageTT01 import login
from Pages.User_actions_pageTT03 import user_actions
from Utils.config import ConfigReader


class Test_checkout_forms():
    # Reading the username from a config file using ConfigReader class
    username = ConfigReader.read_config("loginfo", "user")
    # Reading the password from a config file using ConfigReader class
    password = ConfigReader.read_config("loginfo", "password")
    # Creating a list of tuples where each tuple contains a username and password pair for login
    users = [(username, password)]
    # Declaring 'product' as a global variable so it can be accessed across methods
    global product
    # Declaring 'Login' as a global variable so it can be accessed across methods
    global Login
    global Sort

    global Checkout

    @allure.severity(Severity.CRITICAL)
    @allure.title("Change user password - Test A01")
    @allure.description("logging in,Navigates to my account page,navigate to change password page,and change password")
    @pytest.mark.parametrize("username,password,", users)
    def test_Complete_order_test(self, username, password):
        product = Choose_product(self.driver)
        Login = login(self.driver)
        user = user_actions(self.driver)
        Checkout=Checkoutforms(self.driver)
        with allure.step("Login page steps"):
            Login.menu_button()
            Login.wait(2)
            Login.login_L01()
            Login.wait(2)
            Login.fill_info(username, password)
            Login.wait(2)
            Login.loginbtn()
        with allure.step("Choose product category"):
            product.delay(5)
            product.choose_category("Desktops")
            product.delay(5)
        with allure.step("Choose product"):
            product.delay(5)
            product.choose_product("HP LP3065")
        with allure.step("add to cart"):
            product.delay(5)
            product.add_to_cart()
            product.delay(5)
            product.naviagte_to_cart()
            product.delay(5)
        with allure.step("Checkout button"):
            Checkout.delay(3)
            Checkout.checkout()
        with allure.step("Checkout - Billing details"):
            Checkout.delay(3)
            Checkout.billing_details("13701")
        with allure.step("Delivery details"):
            Checkout.delay(3)
            Checkout.delivery_details("14250")
        with allure.step("Delivery method"):
            Checkout.delay(4)
            Checkout.delivery_method("UPS Delivery method")
        with allure.step("Payment method"):
            Checkout.delay(4)
            Checkout.Payment_method("Method one")
        with allure.step("Confirm Order"):
            Checkout.delay(4)
            Checkout.confirm_order()
            Checkout.delay(6)
            if Checkout.confirm_order_validation():
                assert True
            assert False
#_____________________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Fill and send contact us form - Test A02")
    @allure.description("logging in,Navigates to Contact us page,fill the form and send it")
    @pytest.mark.parametrize("username,password,", users)
    def test_Contact_us_form(self, username, password):
        Login = login(self.driver)
        Checkout=Checkoutforms(self.driver)
        with allure.step("Login page steps"):
            Login.menu_button()
            Login.wait(2)
            Login.login_L01()
            Login.wait(2)
            Login.fill_info(username, password)
            Login.wait(2)
            Login.loginbtn()
        with allure.step("Navigate to contact us page"):
            # contact_us_page
            Checkout.delay(5)
            Checkout.contact_us_page()
            Checkout.delay(5)
        with allure.step("Fill the form"):
            Checkout.delay(4)
            Checkout.Contact_us_form("jaber33423","jaber@xsense.co","dasdsadkukkukuku")
            Checkout.delay(5)
            Checkout.submit()
            Checkout.delay(12)
            if Checkout.contact_form_validation():
                assert True
            else:
             assert False,"one of the fields missing or has invalid Format"

