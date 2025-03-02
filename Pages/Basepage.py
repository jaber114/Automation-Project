import time
from operator import truediv

from attr import attributes
from select import select
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v111.memory import prepare_for_leak_detection
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from Utils.config import ConfigReader
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver:WebDriver=driver

    def delay(self,milliseconds):
        time.sleep(milliseconds)

    def Menu(self,btn_path):
        self.delay(10)
        print(btn_path)
        self.driver.find_element(*btn_path).click()

    def get_url(self):
        return self.driver.current_url

    def login_step(self,btn_path):
        self.delay(3)
        self.driver.find_element(*btn_path).click()

    def sign_out(self,btn):
        self.delay(3)
        self.driver.find_element(*btn).click()
    def logbtn(self,path):
        time.sleep(3)
        self.driver.find_element(*path).click()

    def errmsg(self,msg_path):
        return self.driver.find_element(*msg_path).text
    def fill_login_form(
    self,
    email_path,
    password_path,
    email_value,
    password_value
    ):
        self.driver.find_element(*email_path).clear()
        self.delay(3)
        self.driver.find_element(*email_path).send_keys(*email_value)
        self.delay(3)
        self.driver.find_element(*password_path).clear()
        self.driver.find_element(*password_path).send_keys(*password_value)
        self.delay(3)

    def highlight_element(self, locator, color):
        element = self.driver.find_element(*locator)
        original_style = element.get_attribute("style")
        new_style = "background-color: " + color + ";" + original_style

        # Change the style temporarily
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)

        # Change the style back after a few milliseconds
        self.driver.execute_script("setTimeout(function () { arguments[0].setAttribute('style', arguments[1]); }, 400);"
                                   , element, original_style)
    def signup_page(self,path):
        self.delay(5)
        self.driver.find_element(*path).click()

    def fill_signup_form(
    self,
    first_name,
    first_namepath,
    last_name,
    last_namepath,
    email,
    email_path,
    telephone,
    telephone_path,
    password,
    password_path,
    confirm_value,
    confirm_path
    ):
        self.driver.find_element(*first_namepath).clear()
        self.delay(2)
        self.driver.find_element(*first_namepath).send_keys(*first_name)
        self.delay(2)
        self.driver.find_element(*last_namepath).clear()
        self.delay(2)
        self.driver.find_element(*last_namepath).send_keys(*last_name)
        self.delay(2)
        self.driver.find_element(*email_path).clear()
        self.delay(2)
        self.driver.find_element(*email_path).send_keys(*email)
        self.delay(2)
        self.driver.find_element(*telephone_path).clear()
        self.delay(2)
        self.driver.find_element(*telephone_path).send_keys(*telephone)
        self.delay(2)
        self.driver.find_element(*password_path).clear()
        self.delay(2)
        self.driver.find_element(*password_path).send_keys(*password)
        self.delay(2)
        self.driver.find_element(*confirm_path).clear()
        self.delay(2)
        self.driver.find_element(*confirm_path).send_keys(*confirm_value)
        self.pass_confirm(
        confirm_value,password
        )


    def signup_message(self,message_path):
        message=ConfigReader.read_config("signup","success_message")
        message_url=ConfigReader.read_config("signup","success_url")
        displayed_message=self.driver.find_element(*message_path).text
        return message==displayed_message & message_url==self.driver.current_url

    def pass_confirm(self,confirm_password,password):
        return password==confirm_password

    def check(self,path):
        self.delay(2)
        self.driver.find_element(*path).click()

    def register(self,path):
        self.delay(2)
        self.driver.find_element(*path).click()


    def choose_without_dropdown(self,path,name):
        names=self.driver.find_elements(*path)
        print("without drop down")
        try:
         for i in names:
            if i.text==name:
                i.click()
        except Exception:
           print("")

    def choose_with_dropdown(self, catname, category):
        self.delay(5)
        print("with dropdown")
        try:
            cat_links = self.driver.find_elements(*catname)

            for i in cat_links:
                self.delay(5)

                if i.text == category:
                    self.delay(5)
                    i.click()  # Click on the category
                    self.delay(5)  # Wait for the page to load after click

                    # Look for the 'Show All' button within the clicked category
                    show_allbutton = i.find_elements(By.CSS_SELECTOR, ".see-all")
                    self.delay(5)

                    if show_allbutton:
                        for j in show_allbutton:
                            if j.text == "Show All" + category:
                                # Check if the "Show All" button is visible and clickable
                                if j.is_displayed() and j.is_enabled():
                                    j.click()  # Click the 'Show All' button
                                    self.delay(3)  # Wait for the action to be processed
                                break  # Break after the first valid click (if applicable)
                    break  # Exit the loop once the correct category is found and clicked

        except Exception:
            return

    # def choose_with_dropdown(self,catname,category):
    #   try:
    #     cat_links=self.driver.find_elements(*catname)
    #     for i in cat_links:
    #         if i.text==category:
    #             i.click()
    #             self.delay(5)
    #             show_allbutton=i.find_elements(By.CSS_SELECTOR,".see-all")
    #             for j in show_allbutton:
    #                 if j.text=="Show All"+category:
    #                     j.click()
    #                     break

      # except Exception:
      #     print("")


    # def choose_with_dropdown(self,path,catname,see_allbtn):
    #     see_all=self.driver.find_elements(*see_allbtn)
    #     urls=["https://tutorialsninja.com/demo/index.php?route=product/category&path=34","https://tutorialsninja.com/demo/index.php?route=product/category&path=20","https://tutorialsninja.com/demo/index.php?route=product/category&path=18","https://tutorialsninja.com/demo/index.php?route=product/category&path=25"]
    #     cat_names=self.driver.find_elements(*path)
    #     try:
    #      for i in cat_names:
    #         if i.text==catname:
    #             self.delay(4)
    #             url = i.get_attribute('href')
    #             if url in urls:
    #                 self.delay(4)
    #                 element = self.driver.find_element(By.CSS_SELECTOR, f"a[href='{url}']")
    #                 self.delay(4)
    #                 # self.driver.execute_script("arguments[0].click();", element)
    #                 element.click()
    #                 self.delay(4)
    #                 for k in see_all:
    #                     if k.text=="Show All"+""+catname:
    #                         self.delay(4)
    #                         print("yes")
    #                         k.click()
    #                         return
    #
    #     except StaleElementReferenceException:
    #         print("")
    #     except ElementClickInterceptedException:
    #          return




    def search(self,search_value,search_btn,search_field):
         self.delay(5)
         self.driver.find_element(*search_field).clear()
         self.delay(2)
         self.driver.find_element(*search_field).send_keys(*search_value)
         self.delay(3)
         self.driver.find_element(*search_btn).click()

    def currency_change(self,currency_value,currency_btn,currency_select):
        self.delay(3)
        self.driver.find_element(*currency_btn).click()
        self.delay(3)
        currencies=self.driver.find_elements(*currency_select)
        for i in currencies:
            if i.text=="$US Dollar" or "€Euro" or "£Pound Sterling":
                i.click()
            else:

             self.driver.execute_script("alert('Currency you selected is not supported');")
        self.delay(56)


    def validate_category_name(self,cat_name_onpage,cat_name):
       onpage_cat=self.driver.find_element(*cat_name_onpage).text
       return onpage_cat==cat_name
    def choose_prd(self,prd_name,cart_path):
        try:
            products = self.driver.find_elements(*cart_path)
            for i in products:
                if i.text==prd_name:
                    i.click()
            print("the wanted product is not found")
        except StaleElementReferenceException:
            print("")
    def prd_validationm(self,prdname):
            print(prdname)
            if str(prdname) in self.driver.page_source:
                return True
            else:
                return False

    def prd_valid_search(self,prdname,prdnames):
        products=self.driver.find_elements(*prdnames)
        prdname_lower=prdname.lower()
        prdname_upper=prdname.upper()
        prdname_capitalize=prdname.capitalize()
        for i in products:
            if prdname in i.text or prdname==i.text or prdname_lower in i.text or prdname_lower==i.text :
                return True
        return False

    def add_to_crt(self,cartbtn):
        self.delay(5)
        self.driver.find_element(*cartbtn).click()

    def prd_validate(self,prdname,text_path):
        text=self.driver.find_element(*text_path)
        if(text==prdname & text.is_displayed()):
            return True
        return False

    def delete_prd_from_cart(self,prdname,deletebtn):
        products_in_cart=self.driver.find_elements(By.TAG_NAME,'a')
        delete=self.driver.find_element(*deletebtn)
        for i in products_in_cart:
            if i.text==prdname:
                delete.click()
        print("the wanted product not found in the cart")


    def cart_navigate(self,actionbtn,cartbtn):
        self.delay(2)
        self.driver.find_element(*actionbtn).click()
        self.delay(4)
        self.driver.find_element(*cartbtn).click()

    def deleteall(self,deletebtn):
        delete=self.driver.find_elements(*deletebtn)
        try:
         for i in delete:
             i.click()
        except Exception:
             print("")

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def instock_check(self,stock_text):
        text=self.driver.find_element(*stock_text).text
        if text=="Availability:Out Of Stock":
            return False
        return True

    def update_product_qty(self,quantity_value,quantity_field,quantity_button):
        self.delay(4)
        self.driver.find_element(*quantity_field).clear()
        self.delay(2)
        self.driver.find_element(*quantity_field).send_keys(quantity_value)
        self.delay(2)
        self.driver.find_element(*quantity_button).click()

    def add_prd_wishlist(self,addbtn):
        self.delay(5)
        self.driver.find_element(*addbtn).click()

    def prd_validate_wishlist(self,prdname,links):
     try:
        self.delay(5)
        print(prdname)
        products_names=self.driver.find_elements(*links)
        flag=False
        for i in products_names:
            if i.text==prdname:
                flag=True
            else:
                print("no")
        return flag
     except StaleElementReferenceException:
         print("")

    def valid_qty(self,qty_field,qty_value):
        self.delay(5)
        quantity_field=self.driver.find_element(*qty_field)
        value = quantity_field.get_attribute('value')
        return value==qty_value
    def delete_frm_wishlist(self,prdname,products):
        product_names=self.driver.find_elements(*products)
        url1="https://tutorialsninja.com/demo/index.php?route=account/wishlist&remove="
        try:
         for i in product_names:
            if i.text==prdname:

                    url = i.get_attribute('href')
                    last_chars=url[-2:]
                    # You can process the URL further here, e.g., by constructing the delete URL
                    delete_url = url1 + last_chars
                # Example to find a link by its href URL using XPath

                    element = self.driver.find_element(By.XPATH, f"//a[@href='{delete_url}']")
                    self.delay(5)
                    element.click()
        except StaleElementReferenceException:
                    print("")
        except Exception:
                    print("")

    def navigate_towishlist(self,path):
        self.delay(5)
        self.driver.find_element(*path).click()

    def wrt_review(self,
    name,
    name_field,
    text,
    text_field,
    rating_number,
    rate_field,
    rate_button
     ):
        self.delay(5)
        self.driver.find_element(*name_field).clear()
        self.delay(5)
        self.driver.find_element(*name_field).send_keys(name)
        self.delay(5)
        self.driver.find_element(*text_field).clear()
        self.delay(5)
        self.driver.find_element(*text_field).send_keys(text)
        self.delay(5)
        rating_numbers=self.driver.find_elements(*rate_field)
        for i in rating_numbers:
            input_value = i.get_attribute('value')
            if input_value==rating_number:
                i.click()
        self.delay(6)
        self.driver.find_element(*rate_button).click()


    def click_review(self,btn):
        self.delay(5)
        self.driver.find_element(*btn).click()

    def valid_review(self,errormsg):
        try:
            self.delay(5)
            message=self.driver.find_element(*errormsg).text
            error_messages=[
            "Warning: Review Name must be between 3 and 25 characters!",
            "Warning: Review Text must be between 25 and 1000 characters!",
            "Warning: Please select a review rating!"
            ]
            if message in error_messages:
                return False
            return True
        except Exception:
            return True

    def sortbyname_asc(self,selectoptions):
        options=self.driver.find_element(*selectoptions)
        select=Select(options)
        self.delay(4)
        select.select_by_index(1)


    # def nameAZvalidate(self,links_text):
    #     array_links=[]
    #     texts=[]
    #     likns=self.driver.find_elements(*links_text)
    #     index = 0
    #     index1=0
    #     for i in likns:
    #         url = i.get_attribute('href')
    #         last_chars = url[-23:]
    #         new_url = url.replace(last_chars, "")
    #         element = self.driver.find_element(By.XPATH, f"//a[@href='{new_url}']")
    #         # Insert the link element into the array
    #         array_links.append(element)
    #
    #         # Extract the text of the link and add to texts list
    #         texts.append(i.text)
    #
    #         # Print the link elements (you can modify this part if needed)
    #     print("Link elements:", array_links)
    #
    #     # Print the text of the links
    #     print("Link texts:", texts)
    def change_pass(self,
    password_field,
    confirm_passfield,
    continue_button,
    password):
        self.delay(4)
        self.driver.find_element(*password_field).clear()
        self.delay(2)
        self.driver.find_element(*password_field).send_keys(password)
        self.delay(3)
        self.driver.find_element(*confirm_passfield).clear()
        self.delay(3)
        self.driver.find_element(*confirm_passfield).send_keys(password)
        self.delay(4)
        self.driver.find_element(*continue_button).click()

    def navigate_to_myacc_page(self,myaccbtn):
        self.delay(3)
        self.driver.find_element(*myaccbtn).click()


    def navigate_to_changepsspage(self,changepassbtn):
        self.delay(3)
        self.driver.find_element(*changepassbtn).click()

    def changepassvalidation(self,error_message1,error_message2):
        try:
            self.delay(3)
            message1=self.driver.find_element(*error_message1).text
            message2=self.driver.find_element(*error_message2).text
            if str(message1) in self.driver.page_source or str(message2) in self.driver.page_source:
                return False
            return True
        except Exception:
            return True
    def update_user_info(self,
    first_name_field,
    last_name_field,
    Email_field,
    Phone_field,
    first_name,
    last_name,
    Email,
    Phone,
    continue_button
    ):
        self.delay(3)
        self.driver.find_element(*first_name_field).clear()
        self.delay(2)
        self.driver.find_element(*first_name_field).send_keys(*first_name)
        self.delay(2)
        self.driver.find_element(*last_name_field).clear()
        self.delay(3)
        self.driver.find_element(*last_name_field).send_keys(*last_name)
        self.delay(3)
        self.driver.find_element(*Email_field).clear()
        self.delay(2)
        self.driver.find_element(*Email_field).send_keys(*Email)
        self.delay(3)
        self.driver.find_element(*Phone_field).clear()
        self.delay(4)
        self.driver.find_element(*Phone_field).send_keys(*Phone)
        self.delay(3)
        self.driver.find_element(*continue_button).click()
    def info_validation(self,input_texts):
     try:
        error_messages=[
        "First Name must be between 1 and 32 characters!",
        "Last Name must be between 1 and 32 characters!",
        "E-Mail Address does not appear to be valid!",
        "Telephone must be between 3 and 32 characters!"
        ]
        texts=self.driver.find_elements(*input_texts)
        for i in texts:
            if i.text in error_messages:
                return False
     except Exception:
         return True
    def edit_page(self,btn):
        self.delay(2)
        self.driver.find_element(*btn).click()


    def newsletter_screen(self,button):
        self.delay(2)
        self.driver.find_element(*button).click()

    def subscribe(self,button,continue_button):
        self.delay(1)
        self.driver.find_element(*button).click()
        self.delay(3)
        self.driver.find_element(*continue_button).click()

    def unsubscribe(self,button,continue_button):
        self.delay(3)
        self.driver.find_element(*button).click()
        self.delay(3)
        self.driver.find_element(*continue_button).click()

    def subscription_validation(self,message_text):
      try:
        text=self.driver.find_element(*message_text).text
        if str(text) in self.driver.page_source:
            return True
      except Exception:
          return False

    def Modify_add_book(self,button):
        self.delay(3)
        self.driver.find_element(*button).click()
    def New_address(self,button):
        self.driver.find_element(*button).click()


    def address_bookvalidation(self,button):
        try:
            self.delay(3)
            text=self.driver.find_element(*button).text
            if text=="Your address has been successfully added":
                return True
        except Exception:
            return False

    def add_address_book(self,
    address_first_namefield,
    address_last_namefield,
    address_field,
    city_field,
    post_code_field,
    country_field,
    region_field,
    firstname,
    last_name,
    address,
    city,
    post_code,
    country,
    region,
    continuebtn
    ):
        self.delay(3)
        self.driver.find_element(*address_first_namefield).clear()
        self.delay(3)
        self.driver.find_element(*address_first_namefield).send_keys(*firstname)
        self.delay(3)
        self.driver.find_element(*address_last_namefield).clear()
        self.delay(3)
        self.driver.find_element(*address_last_namefield).send_keys(*last_name)
        self.delay(3)
        self.driver.find_element(*address_field).clear()
        self.delay(3)
        self.driver.find_element(*address_field).send_keys(*address)
        self.delay(3)
        self.driver.find_element(*city_field).clear()
        self.delay(3)
        self.driver.find_element(*city_field).send_keys(*city)
        self.delay(3)
        self.driver.find_element(*post_code_field).clear()
        self.delay(3)
        self.driver.find_element(*post_code_field).send_keys(*post_code)
    #     country select
        country_options = self.driver.find_element(*country_field)
        select2 = Select(country_options)
        self.delay(4)
        select2.select_by_visible_text(country)
        # Region select
        region_options = self.driver.find_element(*region_field)
        select1 = Select(region_options)
        self.delay(4)
        select1.select_by_visible_text(region)
        self.delay(5)
        self.driver.find_element(*continuebtn).click()
        self.delay(10)




    def delivery_mth(self,textarea,text,contine_btn):
        self.delay(3)
        self.driver.find_element(*textarea).clear()
        self.delay(2)
        self.driver.find_element(*textarea).send_keys(*text)
        self.delay(3)
        self.driver.find_element(*contine_btn).click()



    def pay_method(self,Text_area,terms_checkbox,text,btn):
        self.driver.find_element(*Text_area).clear()
        self.delay(4)
        self.driver.find_element(*Text_area).send_keys(text)
        self.delay(2)
        self.driver.find_element(*terms_checkbox).click()
        self.delay(3)
        self.driver.find_element(*btn).click()



    def bill_details(self,address,continue_btn,option):
        address_options=self.driver.find_element(*address)
        select2 = Select(address_options)
        self.delay(2)
        select2.select_by_value(option)
        self.delay(3)
        self.driver.find_element(*continue_btn).click()


    def delivery_dtls(self,delivery_option,continue_btn,option):
        options=self.driver.find_element(*delivery_option)
        self.delay(4)
        select1=Select(options)
        self.delay(4)
        select1.select_by_value(option)
        self.delay(3)
        self.driver.find_element(*continue_btn).click()

    def pay_validation(self,message):
      try:
        self.delay(2)
        error_message=self.driver.find_element(*message).text
        return error_message=="Warning: You must agree to the Terms & Conditions!"
      except Exception:
          return False


    def order_confirm(self,btn):
        self.delay(2)
        self.driver.find_element(*btn).click()


    def Contact_us(
    self,
    name_field,
    Email_field,
    Enquiry_field,
    name,
    Email,
    Enquiry,
    Submit_button
                   ):
        self.driver.find_element(*name_field).clear()
        self.delay(3)
        self.driver.find_element(*name_field).send_keys(*name)
        self.delay(3)
        self.driver.find_element(*Email_field).clear()
        self.delay(3)
        self.driver.find_element(*Email_field).send_keys(*Email)
        self.delay(3)
        self.driver.find_element(*Enquiry_field).clear()
        self.delay(3)
        self.driver.find_element(*Enquiry_field).send_keys(*Enquiry)
        self.delay(3)
        self.driver.find_element(*Submit_button).click()


    def form_validation(self,txt):
      try:
        self.delay(2)
        text=self.driver.find_element(*txt).text
        if str(text) in self.driver.page_source:
         print("yes")
         return True
      except Exception:
          print("No")
          return False


    def chck_out(self,btn):
        self.delay(3)
        self.driver.find_element(*btn).click()

    def confirm_ordr(self,btn):
        self.driver.find_element(*btn).click()

    def confirm_validation(self,message):
        self.delay(3)
        try:
         return str(self.driver.find_element(*message).text)
        except Exception:
            return False


    def contact_page(self,btn):
        self.delay(3)
        self.driver.find_element(*btn).click()

    def submit_button(self,btn):
      try:
        self.delay(3)
        self.driver.find_element(*btn).click()
      except Exception:
         print("")















    def nameAZvalidate(self, links_text):
        array_links = []
        texts = []

        # Wait for elements to be present on the page (adjust the wait time as needed)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(links_text))
        except:
            print("Elements not found")
            return

        # Find all the link elements based on the passed locator
        links = self.driver.find_elements(*links_text)

        # Check if links are found
        if not links:
            print("No links found")
            return

        # Iterate over the links and get the URL and corresponding text
        for i in links:
            url = i.get_attribute('href')  # Get the 'href' attribute (the URL)

            # Check if the 'href' is valid
            if url:
                print(f"Found URL: {url}")
                # Optionally, modify the URL as you are doing with last_chars if needed
                last_chars = url[-23:]
                new_url = url.replace(last_chars, "")
                print(f"Modified URL: {new_url}")

                # Find the element using the new URL (if this part is necessary)
                try:
                    element = self.driver.find_element(By.XPATH, f"//a[@href='{new_url}']")
                    array_links.append(element)
                    texts.append(i.text)
                except Exception as e:
                    print(f"Error finding element with URL {new_url}: {e}")

        # Print the link elements (you can modify this part if needed)
        print("Link elements:", array_links)

        # Print the text of the links
        print("Link texts:", texts)


















































