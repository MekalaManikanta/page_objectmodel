from selenium import webdriver
from Library import *
from _objects import *
from POM import BasePage

class LoginPage(BasePage.BasePage):

    def __init__(self,driver,email,password):
        self.email=email
        self.password=password
        super().__init__(driver)

    def click_login(self):
        self.wrapper_obj.click_element(BasePageObjects.lnk_loin)

    def enter_email(self):
        self.wrapper_obj.enter_text(LoginPageObjects.txt_email, value="manikantac779@gmail.com")

    def enter_password(self):
        self.wrapper_obj.enter_text(LoginPageObjects.txt_password,value="Mani@098")

    def submit_login(self):
        self.wrapper_obj.click_element(LoginPageObjects.btn_login)

    def logut_page(self):
        self.wrapper_obj.click_element(BasePageObjects.lnk_logout)




