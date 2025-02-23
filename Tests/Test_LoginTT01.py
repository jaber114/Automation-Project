
from collections.abc import Mapping
import allure
import pytest
from allure_commons.types import Severity
from allure_pytest.utils import allure_description, allure_title
from Pages.Login_pageTT01 import login
from Utils.config import ConfigReader


class Test_login():
    # personal user_name
    username = ConfigReader.read_config("loginfo", "user")
    password = ConfigReader.read_config("loginfo", "password")
    Current_url = "https://tutorialsninja.com/demo/index.php?route=account/account"
    users = [
             # Test L07 invalid password & Email
             ("stamnmfsgfd", "dsadnakdssada",Current_url),
             # Test L06 Valid password,empty email
             ("", password, Current_url),
             # Test L05 Valid Email,empty password
             (username, "", Current_url),
             # Test L04 - Valid password,wrong email
             ("wrong", password, Current_url),
             # Test L03 - Valid user name,worng password
             (username, "wrong", Current_url),
             # Test L02 Valid username & Password
             (username, password, Current_url),
             ]

    @allure.severity(Severity.CRITICAL)
    @allure.title("Login step scenarios")
    @allure.description("Login with different login scenarious")
    @pytest.mark.parametrize("username,password,url",users)
    def test_loginL02(self,username,password,url):
        Login=login(self.driver)
        Login.menu_button()
        Login.wait(5)
        Login.login_L01()
        Login.wait(5)
        Login.fill_info(username,password)
        Login.wait(10)
        Login.loginbtn()
        Login.wait(10)
        if(Login.current_url() == url):
            assert True
        else:
            assert False,"Invalid password or email or both"
        # Test L07
        Login.logout()

