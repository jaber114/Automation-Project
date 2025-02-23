import allure
import pytest
from allure_commons.types import Severity
from Pages.Choose_product_PageTT04 import Choose_product
from Pages.Login_pageTT01 import login
from Utils.config import ConfigReader
class Test_choose_product():
# Reading the username from a config file using ConfigReader class
 username = ConfigReader.read_config("loginfo", "user")
# Reading the password from a config file using ConfigReader class
 password = ConfigReader.read_config("loginfo", "password")
# Creating a list of tuples where each tuple contains a username and password pair for login
 users = [(username,password)]
 # Declaring 'product' as a global variable so it can be accessed across methods
 global product
 # Declaring 'Login' as a global variable so it can be accessed across methods
 global Login

 @allure.severity(Severity.MINOR)
 @allure.title("Choose product")
 @allure.description("logging in, then going to cart then logging out")
 @pytest.mark.parametrize("username,password",users)
 # Test C01
 def test_choose_product_category(self,username,password):
        product = Choose_product(self.driver)
        Login = login(self.driver)
        with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
         with allure.step("Choose product category"):
          product.delay(5)
          product.choose_category("Components")
          product.delay(5)
          if(product.validate_catname("Components")==False):
              assert False,"Product category not exist in the website"
          try:
              alert = self.driver.switch_to.alert
              alert_text = alert.text
              if(alert_text.strip()):
               assert False, "Product category not exist in the website"
          except Exception:
              print("")
 #------------------------------------------------------------------------------
 # Test C02
 @allure.severity(Severity.CRITICAL)
 @allure.title("Choose product")
 @allure.description("logging in, then going to cart then logging out")
 @pytest.mark.parametrize("username,password",users)
 def test_Choose_product(self,username,password):
  product = Choose_product(self.driver)
  Login = login(self.driver)
  with allure.step("Login page steps"):
          Login.menu_button()
          Login.wait(5)
          Login.login_L01()
          Login.wait(5)
          Login.fill_info(username, password)
          Login.wait(10)
          Login.loginbtn()
  with allure.step("Choose product category"):
          product.delay(5)
          product.choose_category("Cameras")
          product.delay(5)
  with allure.step("choose product"):
           product.choose_product("Canon EOS 5Da")
           product.delay(5)
           if(product.product_validation==True):
            assert True,"product not found"
           else:
               assert False
 #____________________________________________________________________________________________________________________
 # Test C03
 @allure.severity(Severity.CRITICAL)
 @allure.title("Choose product")
 @allure.description("logging in, searching for product and validating if its displayed in the search results")
 @pytest.mark.parametrize("username,password", users)
 def test_search_product(self, username, password):
     product = Choose_product(self.driver)
     Login = login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("search for product"):
         product.delay(5)
         product.product_search("Mac")
         product.delay(5)
         if(product.validate_product_search("mac")):
             assert True
         else:
             assert False,"your searched product not in the website"
 # Test C04
 @allure.severity(Severity.CRITICAL)
 @allure.title("Choose product")
 @allure.description("logging in, choosing product category,choosing product and adding it to the cart")
 @pytest.mark.parametrize("username,password,",users)
 def test_add_tocart(self,username,password):
     product = Choose_product(self.driver)
     Login = login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("Choose product category"):
         product.delay(5)
         product.choose_category("Phones & PDAs")
         product.delay(5)
     with allure.step("Choose product"):
         product.delay(5)
         product.choose_product("iPhone")
     with allure.step("add to cart"):
         product.delay(5)
         product.add_to_cart()
         product.delay(5)
         product.naviagte_to_cart()
         product.delay(5)
         if(product.product_validation("iPhone")):
             assert True
         else:
          assert False,"the wanted product not added to the cart"
# _______________________________________________________________________________________________________________________________________________________________________
 @allure.severity(Severity.CRITICAL)
 @allure.title("Delete product from cart")
 @allure.description("logging in,choosing product category,choosing product then adding it to the cart and delete it from the cart")
 @pytest.mark.parametrize("username,password,", users)
 # Test C05
 def test_delete_product_from_cart(self,username,password):
     product=Choose_product(self.driver)
     Login=login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("Choose product category"):
         product.delay(5)
         product.choose_category("Phones & PDAs")
         product.delay(5)
     with allure.step("Choose product"):
        product.delay(5)
        product.choose_product("iPhone")
     with allure.step("add to cart"):
         product.delay(5)
         product.add_to_cart()
         product.delay(5)
         product.naviagte_to_cart()
         product.delay(5)
     with allure.step("delete from cart"):
        product.delete_product_from_cart("iPhone")
#_______________________________________________________________________________________________
 # Test C06
 @allure.severity(Severity.CRITICAL)
 @allure.title("Validate product status stock/out of stock")
 @allure.description("logging in,choosing product category,choosing product then adding it to the cart,and check the product status")
 @pytest.mark.parametrize("username,password,",users)
 def test_product_quantity(self,username,password):
     product=Choose_product(self.driver)
     Login=login(self.driver)
     with allure.step("Login page steps"):
              Login.menu_button()
              Login.wait(5)
              Login.login_L01()
              Login.wait(5)
              Login.fill_info(username, password)
              Login.wait(10)
              Login.loginbtn()
     with allure.step("Choose product category"):
         product.delay(5)
         product.choose_category("Phones & PDAs")
         product.delay(5)
     with allure.step("Choose product"):
        product.delay(5)
        product.choose_product("HTC Touch HD")
     with allure.step("Check product availability status(In stock/Out of stock)"):
         product.delay(5)
         if product.product_instock()==True:
             assert True
         else:
             assert False,"the product is out of stock"
#_______________________________________________________________________________________________________________________
 @allure.severity(Severity.CRITICAL)
 @allure.title("Update product quantity")
 @allure.description("logging in,choosing product category,choosing product then adding it to the cart and update its quantity")
 @pytest.mark.parametrize("username,password,", users)
 # Test C07
 def test_Update_product_quantity(self,username,password):
     product=Choose_product(self.driver)
     Login=login(self.driver)
     with allure.step("Login page steps"):
         Login.menu_button()
         Login.wait(5)
         Login.login_L01()
         Login.wait(5)
         Login.fill_info(username, password)
         Login.wait(10)
         Login.loginbtn()
     with allure.step("Choose product category"):
         product.delay(5)
         product.choose_category("Phones & PDAs")
         product.delay(5)
     with allure.step("Choose product"):
        product.delay(5)
        product.choose_product("iPhone")
     with allure.step("add to cart"):
         product.delay(5)
         product.add_to_cart()
         product.delay(5)
         product.naviagte_to_cart()
         product.delay(5)
     with allure.step("update product quantity"):
        product.update_qty(5)
        product.delay(5)
        print(product.validate_quantity_update(5))

#_______________________________________________________________________________________________________________________
 # Test C08
 @allure.severity(Severity.CRITICAL)
 @allure.title("Add product to wishlist")
 @allure.description("logging in,choosing product category,adding product to wishlist")
 @pytest.mark.parametrize("username,password,",users)
 def test_Add_product_towishlist(self, username, password):
    product = Choose_product(self.driver)
    Login = login(self.driver)
    with allure.step("Login page steps"):
        Login.menu_button()
        Login.wait(5)
        Login.login_L01()
        Login.wait(5)
        Login.fill_info(username, password)
        Login.wait(10)
        Login.loginbtn()
    with allure.step("Choose product category"):
        product.delay(5)
        product.choose_category("Phones & PDAs")
        product.delay(5)
    with allure.step("Choose product"):
        product.delay(5)
        product.choose_product("iPhone")
    with allure.step("Add product to wishlist"):
        product.delay(5)
        product.add_product_towishlist()
        product.delay(5)
        if product.wishlist_validation("iPhone")==True:
            assert True
        else:
            assert False,"Product not added to the wishlist"
#________________________________________________________________________________________________
 # Test C09
 @allure.severity(Severity.CRITICAL)
 @allure.title("Add product to wishlist")
 @allure.description("logging in,choosing product category,adding product to wishlist")
 @pytest.mark.parametrize("username,password,",users)
 def test_delete_product_from_wishlist(self, username, password):
    product = Choose_product(self.driver)
    Login = login(self.driver)
    with allure.step("Login page steps"):
            Login.menu_button()
            Login.wait(5)
            Login.login_L01()
            Login.wait(5)
            Login.fill_info(username, password)
            Login.wait(10)
            Login.loginbtn()
    with allure.step("Choose product category"):
        product.delay(5)
        product.choose_category("Phones & PDAs")
        product.delay(5)
    with allure.step("Choose product"):
        product.delay(5)
        product.choose_product("iPhone")
    with allure.step("Add product to wishlist"):
        product.delay(5)
        product.add_product_towishlist()
        product.delay(5)
        product.wishlist_page()
        product.delay(5)
        product.delete_from_wishlist("iPhone")
        product.delay(5)
        if(product.wishlist_validation("iPhone")==True):
            assert True
        else:
            assert False,"the product not deleted from the wishlist"
#_________________________________________________________________________________________________________---
# Test C10
 @allure.severity(Severity.CRITICAL)
 @allure.title("Write product review")
 @allure.description("logging in,choosing product category,adding product to wishlist")
 @pytest.mark.parametrize("username,password,",users)
 def test_Add_product_review(self, username, password):
    product = Choose_product(self.driver)
    Login = login(self.driver)
    with allure.step("Login page steps"):
            Login.menu_button()
            Login.wait(5)
            Login.login_L01()
            Login.wait(5)
            Login.fill_info(username, password)
            Login.wait(10)
            Login.loginbtn()
    with allure.step("Choose product category"):
        product.delay(5)
        product.choose_category("Phones & PDAs")
        product.delay(5)
    with allure.step("Choose product"):
        product.delay(5)
        product.choose_product("iPhone")
    with allure.step("Write product review"):
        product.delay(5)
        product.click_review_btn()
        product.delay(5)
        product.Write_a_review("jaber","asdadajjewrewtertretretretertretrerewrw","2")
        product.delay(10)
        if product.validate_review():
            assert True
        else:
            assert False,"one of the field is invalid take a look at the error message"
#_____________________________________________________________________________________________________________________________________________


















