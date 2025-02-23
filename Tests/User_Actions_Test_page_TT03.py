from itertools import product

import allure
import pytest
from allure_commons.types import Severity

from Pages.Choose_product_PageTT04 import Choose_product
from Pages.Login_pageTT01 import login
from Pages.User_actions_pageTT03 import user_actions
from Utils.config import ConfigReader


class Test_sort():
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
 @allure.severity(Severity.CRITICAL)
 @allure.title("Change user password - Test P01")
 @allure.description("logging in,Navigates to my account page,navigate to change password page,and change password")
 @pytest.mark.parametrize("username,password,", users)
 def test_Change_user_password(self,username,password):
     product = Choose_product(self.driver)
     Login = login(self.driver)
     user=user_actions(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(2)
         Login.login_L01()
         Login.wait(2)
         Login.fill_info(username, password)
         Login.wait(2)
         Login.loginbtn()
     with allure.step("Navigate to user change password screen"):
             user.delay(3)
             user.myaccount_page()
             user.delay(3)
             user.chanepass_page()
             user.delay(21)
     with allure.step("Change user password step"):
             user.change_password("jaberr")
             user.delay(21)
             if user.changepass_validaiton():
                 assert True
             else:
                 assert False,"password not match confirm password or password need more chars"
     #___________________________________________________________________________________________________________________
 @allure.severity(Severity.CRITICAL)
 @allure.title("Update user information Test-P02")
 @allure.description("logging in,Navigates to my account page,navigate to edit user info screen,and change user information")
 @pytest.mark.parametrize("username,password,", users)
 def test_Update_user_information(self,username,password):
     product = Choose_product(self.driver)
     Login = login(self.driver)
     user=user_actions(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(2)
         Login.login_L01()
         Login.wait(2)
         Login.fill_info(username, password)
         Login.wait(2)
         Login.loginbtn()
     with allure.step("Navigate to Edit account information  screen"):
             user.delay(3)
             user.myaccount_page()
             user.delay(3)
             user.Edit_info_page()
             user.delay(3)
     with allure.step("Change user first & lastname,Email and phone"):
             user.change_user_information("j","r","jaber@xsense","2")
             user.delay(21)
             if user.update_info_validation():
                 assert True
             else:
                 assert False,"One of the fields has invalid format"
#_______________________________________________________________________________________________________________________________
 @allure.severity(Severity.MINOR)
 @allure.title("Subscribe to newsletter Test-P03")
 @allure.description("logging in,Navigates to my account page,navigate to subscribe to newsletter  screen,and perform the subscribe action")
 @pytest.mark.parametrize("username,password,", users)
 def test_Subscribe_to_newsletter(self,username,password):
     product = Choose_product(self.driver)
     Login = login(self.driver)
     user=user_actions(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(2)
         Login.login_L01()
         Login.wait(2)
         Login.fill_info(username, password)
         Login.wait(2)
         Login.loginbtn()
     with allure.step("Navigate to Subscribe / unsubscribe to newsletter  screen"):
             user.delay(3)
             user.myaccount_page()
             user.delay(3)
             user.Newsletter_page()
             user.delay(3)
     with allure.step("Subscribe to the newsletter"):
             user.delay(2)
             user.subscribe_to_newsletter()
             user.delay(5)
     if user.validate_subscription():
         assert True
     else:
         assert False, "One of the fields has invalid format"
#__________________________________________________________________________________________________________________
 @allure.severity(Severity.MINOR)
 @allure.title("Unsubscribe to newsletter Test-P04")
 @allure.description("logging in,Navigates to my account page,navigate to subscribe to newsletter  screen,and perform the unsubscribe action")
 @pytest.mark.parametrize("username,password,", users)
 def test_Subscribe_to_newsletter(self, username, password):
     product = Choose_product(self.driver)
     Login = login(self.driver)
     user = user_actions(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(2)
         Login.login_L01()
         Login.wait(2)
         Login.fill_info(username, password)
         Login.wait(2)
         Login.loginbtn()
     with allure.step("Navigate to Subscribe / unsubscribe to newsletter  screen"):
         user.delay(3)
         user.myaccount_page()
         user.delay(3)
         user.Newsletter_page()
         user.delay(3)
     with allure.step("Subscribe to the newsletter"):
         user.delay(2)
         user.unsubscribe_to_newsletter()
         user.delay(5)
     if user.validate_subscription():
         assert True
     else:
         assert False, "One of the fields has invalid format"
 #_________________________________________________________________________________________________________________
 # Test P05
 @allure.severity(Severity.MINOR)
 @allure.title("Add new Book Entries - Test P05")
 @allure.description("logging in,Navigates to my account page,navigate to Modify your address book entries  screen,and perform add new address book entries")
 @pytest.mark.parametrize("username,password,", users)
 def test_Add_book_entries_address(self,username,password):
     product = Choose_product(self.driver)
     Login = login(self.driver)
     user=user_actions(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(2)
         Login.login_L01()
         Login.wait(2)
         Login.fill_info(username, password)
         Login.wait(2)
         Login.loginbtn()
     with allure.step("Navigate to Book Entries new address   screen"):
             user.delay(3)
             user.myaccount_page()
             user.delay(3)
             user.modify_address_book()
             user.delay(3)
             user.New_address_book()
     with allure.step("Add new address book entries"):
             user.delay(2)
             user.add_Address_Book_Entries(
             "jaber",
              "rammal",
              "Roghab street",
              "Yirka",
               "658963",
                 "Israel",
                 "Haifa")
     if user.address_book_entries_validation():
         assert True
     else:
         assert False, "One of the fields has invalid format"
#______________________________________________________________________________________________________________________________________________



