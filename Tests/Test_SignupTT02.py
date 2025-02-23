import allure
import pytest
from allure_commons.types import Severity
from allure_pytest.utils import allure_title

from Pages.Sign_up_pageTT02 import signup
from Utils.config import ConfigReader


class Test_signup():
 success_signup_url=ConfigReader.read_config("Signup_form_error_messages","confirm_email")
 users = [
# Test S02 Invalid first_name format
("", "Rammal","oldscroll14@gmail.com","09256948","pass","pass654",success_signup_url),
# Test S03 Invalid last name format
("asdgfgd", "","oldscroll146@gmail.com","09256948","pass","pass654",success_signup_url),
 # Test S04 Invalid Email format
("jaber", "Rammal","99625dgmail.com","09256948","pass","pass654",success_signup_url),
# Test S05 Invalid password format
("jaber", "Rammal","99625a@gmail.com","09256948","o","o",success_signup_url),
# Test S06 Invalid Phone format
("jaber", "Rammal","99625z@gmail.com","09","oASD","oASd",success_signup_url),
# Test S07 Invalid password confirm
("jaber", "Rammal","99625c@gmail.com","09","oASD","oASd253",success_signup_url),
# Test S08 Valid register format
("jaber", "Rammal", "99625dsa5144@gmail.com", "5655885246", "abera", "abera",success_signup_url),
]
 @allure.severity(Severity.CRITICAL)
 @allure.title("Signup for new users test")
 @allure.description("signup for new users with more than scenario")
 @pytest.mark.parametrize("first_name,last_name,Email,phone,password,passconfirm,url", users)
 def test_signup(self,first_name,last_name,Email,phone,password,passconfirm,url):
     signup_form=signup(self.driver)
     signup_form.menu_button()
     signup_form.delay(5)
     # Test S01
     signup_form.visit_signuppage()
     signup_form.delay(5)
     signup_form.Fill_signup(
         first_name,
         last_name,
         Email,
         phone,
         password,
         passconfirm
         )
     signup_form.delay(3)
     # Test S09
     signup_form.privacy_check()
     signup_form.delay(3)
     # Test S10
     signup_form.Register()
     signup_form.delay(5)
     assert signup_form.current_url()==url,"One or more of the fields are empty or with incorrect value"


