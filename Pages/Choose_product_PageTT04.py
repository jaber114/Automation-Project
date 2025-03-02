from itertools import product

from selenium.webdriver.common.by import By

from Pages.Basepage import BasePage
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.alert import Alert


class Choose_product(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
    cat_names = (By.TAG_NAME,'a')
    Showall_products = (By.CSS_SELECTOR,".see-all")
    search_field = (By.CSS_SELECTOR,"#search > input")
    search_btn= (By.CSS_SELECTOR,"#search > span > button")
    category_names=["Desktops","Laptops & Notebooks","Components","Tablets","Software","Phones & PDAs","Cameras","MP3 Players"]
    currency_btn = (By.CSS_SELECTOR,"#form-currency > div > button > span")
    currency_select = (By.CSS_SELECTOR,".currency-select")
    Category_name_onpage = (By.CSS_SELECTOR,"#content > h2")
    currency_validation = (By.CSS_SELECTOR,"#content > div.row > div:nth-child(1) > div > div.caption > p.price")
    product_validation= (By.CSS_SELECTOR,"#content > div > div.col-sm-4 > h1")
    Add_to_cart_btn = (By.CSS_SELECTOR,"#button-cart")
    delete_from_cart_btn = (By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > td:nth-child(4) > div > span > button.btn.btn-danger")
    product_actions_button=(By.CSS_SELECTOR,"#cart > button")
    cart_button=(By.CSS_SELECTOR,"#cart > ul > li:nth-child(2) > div > p > a:nth-child(1)")
    Product_stock_text = (By.CSS_SELECTOR,"#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(3) > li:nth-child(3)")
    delete_all_btn= (By.CSS_SELECTOR,".input-group-btn>button.btn.btn-danger")
    quantity_field = (By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > td:nth-child(4) > div > input")
    quantity_button= (By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > td:nth-child(4) > div > span > button.btn.btn-primary")
    wishlist_button = (By.CSS_SELECTOR,"#wishlist-total > span")
    rating_name=(By.CSS_SELECTOR,"#input-name")
    rating_text=(By.CSS_SELECTOR,"#input-review")
    rating_number = (By.CSS_SELECTOR,".col-sm-12>[type=radio]")
    Write_review_button = (By.CSS_SELECTOR,"#content > div:nth-child(1) > div.col-sm-4 > div.rating > p > a:nth-child(7)")
    rating_error_msg=(By.CSS_SELECTOR,"#form-review > div.alert.alert-danger.alert-dismissible")
    submit_rating_button = (By.CSS_SELECTOR,"#button-review")
    dropdown=(By.CSS_SELECTOR,".dropdown")
    add_to_wishlist=(By.CSS_SELECTOR,"#content > div > div.col-sm-4 > div.btn-group > button:nth-child(1)")
    def choose_category(self,category):
        if category in self.category_names:
            if category=="Desktops" or "MP3 Players" or "Laptops & Notebooks" or "Components":
             self.choose_with_dropdown(self.dropdown, category)
            elif category=="Cameras" or "Tablets" or "Software" or "Phones & PDAs":
               self.choose_without_dropdown(self.cat_names,category)
        else:
            self.driver.execute_script("alert('you choose categorie that is not exist');")

    def product_search(self,prd_name):
        self.delay(5)
        self.search(prd_name,self.search_btn,self.search_field)

    def change_currency(self,currency):
        self.currency_change(currency,self.currency_btn,self.currency_select)
    def validate_catname(self,category):
        self.delay(5)
        return self.validate_category_name(self.Category_name_onpage,category)
    def choose_product(self,prd_name):
        self.choose_prd(prd_name,self.cat_names)
    def product_validation(self,prd_name):
        self.delay(5)
        # self.prd_validate(prd_name,self.product_validation)
        return self.prd_validationm(prd_name)
    def validate_product_search(self,name):
        self.delay(5)
        return self.prd_valid_search(name,self.cat_names)
    def add_to_cart(self):
        self.add_to_crt(self.Add_to_cart_btn)


    def product_available_check(self):
        return self.prd_validate(self.Product_stock_text)

    def delete_product_from_cart(self,prdname):
        self.delete_prd_from_cart(prdname,self.delete_from_cart_btn)

    def delete_all_from_cart(self):
        self.deleteall(self.delete_all_btn)

    def naviagte_to_cart(self):
        self.delay(5)
        self.cart_navigate(self.product_actions_button,self.cart_button)

    def product_instock(self):
        return self.instock_check(self.Product_stock_text)

    def update_qty(self,qtyvalue):
        self.delay(5)
        self.update_product_qty(qtyvalue,self.quantity_field,self.quantity_button)
        self.delay(4)

    def validate_quantity_update(self,qtyvalue):
        self.delay(5)
        return self.valid_qty(self.quantity_field,qtyvalue)

    def add_product_towishlist(self):
        self.delay(5)
        self.add_prd_wishlist(self.add_to_wishlist)
    def wishlist_validation(self,prdname):
        self.delay(5)
        return self.prd_validate_wishlist(prdname,self.cat_names)
    def wishlist_page(self):
        self.navigate_towishlist(self.wishlist_button)
    def delete_from_wishlist(self,prdname):
        self.delay(5)
        self.delete_frm_wishlist(prdname,self.cat_names)


    def Write_a_review(self,name,review_text,rating_number):
            textlen=len(review_text)
            self.wrt_review(
            name,
            self.rating_name,
            review_text,
            self.rating_text,
            rating_number,
            self.rating_number,
            self.submit_rating_button
            )


    def click_review_btn(self):
        self.click_review(self.Write_review_button)

    def validate_review(self):
        self.delay(4)
        return self.valid_review(self.rating_error_msg)


















