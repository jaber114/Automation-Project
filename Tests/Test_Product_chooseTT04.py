import allure
import pytest
from allure_commons.types import Severity
from Pages.Choose_product_page_PageTT04 import Choose_product_page
from Pages.Login_pageTT01 import login
from Utils.config import ConfigReader
class Test_choose_product_page():
# Reading the username from a config file using ConfigReader class
 username = ConfigReader.read_config("loginfo", "user")
# Reading the password from a config file using ConfigReader class
 password = ConfigReader.read_config("loginfo", "password")
# Creating a list of tuples where each tuple contains a username and password pair for login
 users = [(username,password)]
 # Declaring 'product_page' as a global variable so it can be accessed across methods
 global product_page
 # Declaring 'Login' as a global variable so it can be accessed across methods
 global Login

 @allure.severity(Severity.MINOR)
 @allure.title("Choose product_page")
 @allure.description("logging in, then going to cart then logging out")
 @pytest.mark.parametrize("username,password",users)
 # Test C01
 def test_choose_product_page_category(self,username,password):
        product_page = Choose_product_page(self.driver)
        Login = login(self.driver)
        with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
         with allure.step("Choose product_page category"):
          product_page.delay(5)
          product_page.choose_category("Components")
          product_page.delay(5)
          if(product_page.validate_catname("Components")==False):
              assert False,"product_page category not exist in the website"
          try:
              alert = self.driver.switch_to.alert
              alert_text = alert.text
              if(alert_text.strip()):
               assert False, "product_page category not exist in the website"
          except Exception:
              print("")
 #------------------------------------------------------------------------------
 # Test C02
 @allure.severity(Severity.CRITICAL)
 @allure.title("Choose product_page")
 @allure.description("logging in, then going to cart then logging out")
 @pytest.mark.parametrize("username,password",users)
 def test_Choose_product_page(self,username,password):
  product_page = Choose_product_page(self.driver)
  Login = login(self.driver)
  with allure.step("Login page steps"):
          Login.menu_button()
          Login.wait(5)
          Login.login_L01()
          Login.wait(5)
          Login.fill_info(username, password)
          Login.wait(10)
          Login.loginbtn()
  with allure.step("Choose product_page category"):
          product_page.delay(5)
          product_page.choose_category("Cameras")
          product_page.delay(5)
  with allure.step("choose product_page"):
           product_page.choose_product_page("Canon EOS 5Da")
           product_page.delay(5)
           if(product_page.product_page_validation==True):
            assert True,"product_page not found"
           else:
               assert False
 #____________________________________________________________________________________________________________________
 # Test C03
 @allure.severity(Severity.CRITICAL)
 @allure.title("Choose product_page")
 @allure.description("logging in, searching for product_page and validating if its displayed in the search results")
 @pytest.mark.parametrize("username,password", users)
 def test_search_product_page(self, username, password):
     product_page = Choose_product_page(self.driver)
     Login = login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("search for product_page"):
         product_page.delay(5)
         product_page.product_page_search("Mac")
         product_page.delay(5)
         if(product_page.validate_product_page_search("mac")):
             assert True
         else:
             assert False,"your searched product_page not in the website"
 # Test C04
 @allure.severity(Severity.CRITICAL)
 @allure.title("Choose product_page")
 @allure.description("logging in, choosing product_page category,choosing product_page and adding it to the cart")
 @pytest.mark.parametrize("username,password,",users)
 def test_add_tocart(self,username,password):
     product_page = Choose_product_page(self.driver)
     Login = login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("Choose product_page category"):
         product_page.delay(5)
         product_page.choose_category("Phones & PDAs")
         product_page.delay(5)
     with allure.step("Choose product_page"):
         product_page.delay(5)
         product_page.choose_product_page("iPhone")
     with allure.step("add to cart"):
         product_page.delay(5)
         product_page.add_to_cart()
         product_page.delay(5)
         product_page.naviagte_to_cart()
         product_page.delay(5)
         if(product_page.product_page_validation("iPhone")):
             assert True
         else:
          assert False,"the wanted product_page not added to the cart"
# _______________________________________________________________________________________________________________________________________________________________________
 @allure.severity(Severity.CRITICAL)
 @allure.title("Delete product_page from cart")
 @allure.description("logging in,choosing product_page category,choosing product_page then adding it to the cart and delete it from the cart")
 @pytest.mark.parametrize("username,password,", users)
 # Test C05
 def test_delete_product_page_from_cart(self,username,password):
     product_page=Choose_product_page(self.driver)
     Login=login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("Choose product_page category"):
         product_page.delay(5)
         product_page.choose_category("Phones & PDAs")
         product_page.delay(5)
     with allure.step("Choose product_page"):
        product_page.delay(5)
        product_page.choose_product_page("iPhone")
     with allure.step("add to cart"):
         product_page.delay(5)
         product_page.add_to_cart()
         product_page.delay(5)
         product_page.naviagte_to_cart()
         product_page.delay(5)
     with allure.step("delete from cart"):
        product_page.delete_product_page_from_cart("iPhone")
#_______________________________________________________________________________________________
 # Test C06
 @allure.severity(Severity.CRITICAL)
 @allure.title("Validate product_page status stock/out of stock")
 @allure.description("logging in,choosing product_page category,choosing product_page then adding it to the cart,and check the product_page status")
 @pytest.mark.parametrize("username,password,",users)
 def test_product_page_quantity(self,username,password):
     product_page=Choose_product_page(self.driver)
     Login=login(self.driver)
     with allure.step("Login page steps"):
              Login.menu_button()
              Login.wait(5)
              Login.login_L01()
              Login.wait(5)
              Login.fill_info(username, password)
              Login.wait(10)
              Login.loginbtn()
     with allure.step("Choose product_page category"):
         product_page.delay(5)
         product_page.choose_category("Phones & PDAs")
         product_page.delay(5)
     with allure.step("Choose product_page"):
        product_page.delay(5)
        product_page.choose_product_page("HTC Touch HD")
     with allure.step("Check product_page availability status(In stock/Out of stock)"):
         product_page.delay(5)
         if product_page.product_page_instock()==True:
             assert True
         else:
             assert False,"the product_page is out of stock"
#_______________________________________________________________________________________________________________________
 @allure.severity(Severity.CRITICAL)
 @allure.title("Update product_page quantity")
 @allure.description("logging in,choosing product_page category,choosing product_page then adding it to the cart and update its quantity")
 @pytest.mark.parametrize("username,password,", users)
 # Test C07
 def test_Update_product_page_quantity(self,username,password):
     product_page=Choose_product_page(self.driver)
     Login=login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("Choose product_page category"):
         product_page.delay(5)
         product_page.choose_category("Phones & PDAs")
         product_page.delay(5)
     with allure.step("Choose product_page"):
        product_page.delay(5)
        product_page.choose_product_page("iPhone")
     with allure.step("add to cart"):
         product_page.delay(5)
         product_page.add_to_cart()
         product_page.delay(5)
         product_page.naviagte_to_cart()
         product_page.delay(5)
     with allure.step("update product_page quantity"):
        product_page.update_qty(5)
        product_page.delay(5)
        print(product_page.validate_quantity_update(5))

#_______________________________________________________________________________________________________________________
 # Test C08
 @allure.severity(Severity.CRITICAL)
 @allure.title("Add product_page to wishlist")
 @allure.description("logging in,choosing product_page category,adding product_page to wishlist")
 @pytest.mark.parametrize("username,password,",users)
 def test_Add_product_page_towishlist(self, username, password):
    product_page = Choose_product_page(self.driver)
    Login = login(self.driver)
    with allure.step("Login page steps"):
        Login.menu_button()
        Login.wait(5)
        Login.login_L01()
        Login.wait(5)
        Login.fill_info(username, password)
        Login.wait(10)
        Login.loginbtn()
    with allure.step("Choose product_page category"):
        product_page.delay(5)
        product_page.choose_category("Phones & PDAs")
        product_page.delay(5)
    with allure.step("Choose product_page"):
        product_page.delay(5)
        product_page.choose_product_page("iPhone")
    with allure.step("Add product_page to wishlist"):
        product_page.delay(5)
        product_page.add_product_page_towishlist()
        product_page.delay(5)
        if product_page.wishlist_validation("iPhone")==True:
            assert True
        else:
            assert False,"product_page not added to the wishlist"
#________________________________________________________________________________________________
 # Test C09
 @allure.severity(Severity.CRITICAL)
 @allure.title("Add product_page to wishlist")
 @allure.description("logging in,choosing product_page category,adding product_page to wishlist")
 @pytest.mark.parametrize("username,password,",users)
 def test_delete_product_page_from_wishlist(self, username, password):
    product_page = Choose_product_page(self.driver)
    Login = login(self.driver)
    with allure.step("Login page steps"):
            Login.menu_button()
            Login.wait(5)
            Login.login_L01()
            Login.wait(5)
            Login.fill_info(username, password)
            Login.wait(10)
            Login.loginbtn()
    with allure.step("Choose product_page category"):
        product_page.delay(5)
        product_page.choose_category("Phones & PDAs")
        product_page.delay(5)
    with allure.step("Choose product_page"):
        product_page.delay(5)
        product_page.choose_product_page("iPhone")
    with allure.step("Add product_page to wishlist"):
        product_page.delay(5)
        product_page.add_product_page_towishlist()
        product_page.delay(5)
        product_page.wishlist_page()
        product_page.delay(5)
        product_page.delete_from_wishlist("iPhone")
        product_page.delay(5)
        if(product_page.wishlist_validation("iPhone")==True):
            assert True
        else:
            assert False,"the product_page not deleted from the wishlist"
#_________________________________________________________________________________________________________---
# Test C10
 @allure.severity(Severity.CRITICAL)
 @allure.title("Write product_page review")
 @allure.description("logging in,choosing product_page category,adding product_page to wishlist")
 @pytest.mark.parametrize("username,password,",users)
 def test_Add_product_page_review(self, username, password):
    product_page = Choose_product_page(self.driver)
    Login = login(self.driver)
    with allure.step("Login page steps"):
            Login.menu_button()
            Login.wait(5)
            Login.login_L01()
            Login.wait(5)
            Login.fill_info(username, password)
            Login.wait(10)
            Login.loginbtn()
    with allure.step("Choose product_page category"):
        product_page.delay(5)
        product_page.choose_category("Phones & PDAs")
        product_page.delay(5)
    with allure.step("Choose product_page"):
        product_page.delay(5)
        product_page.choose_product_page("iPhone")
    with allure.step("Write product_page review"):
        product_page.delay(5)
        product_page.click_review_btn()
        product_page.delay(5)
        product_page.Write_a_review("jaber","asdadajjewrewtertretretretertretrerewrw","2")
        product_page.delay(10)
        if product_page.validate_review():
            assert True
        else:
            assert False,"one of the field is invalid take a look at the error message"
#_____________________________________________________________________________________________________________________________________________


















