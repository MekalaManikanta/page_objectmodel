from selenium import webdriver
from Library.selenium_wrapper import SeleniumWrapper
from _objects import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper_obj = SeleniumWrapper(self.driver)

    def Register_link(self):
        self.wrapper_obj.click_element(BasePageObjects.lnk_register)

    def login_link(self):
        self.wrapper_obj.click_element(BasePageObjects.lnk_login)

    def shopping_cart_link(self):
        self.wrapper_obj.click_element(BasePageObjects.lnk_shopping_cart)

