from selenium import webdriver
from Library import *
from _objects import *
from POM import BasePage


class RegisterationPage(BasePage.BasePage):

    def __init__(self, driver, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        super().__init__(driver)

    def click_male_radio_button(self):
        self.wrapper_obj.click_element(RegistrationPageObjects.rdo_male)

    def click_female_radio_button(self):
        self.wrapper_obj.click_element(RegistrationPageObjects.rdo_female)

    def enter_firstname(self):
        self.wrapper_obj.enter_text(RegistrationPageObjects.txt_firstname, value=self.fname)

    def enter_lastname(self):
        self.wrapper_obj.enter_text(RegistrationPageObjects.txt_lastname, value=self.lname)

    def enter_email(self):
        self.wrapper_obj.enter_text(RegistrationPageObjects.txt_email, value=self.email)

    def enter_password(self):
        self.wrapper_obj.enter_text(RegistrationPageObjects.txt_password, value=self.password)

    def confirm_password(self):
        self.wrapper_obj.enter_text(RegistrationPageObjects.txt_confirm_password, value=self.password)

    def click_reg_button(self):
        self.wrapper_obj.click_element(RegistrationPageObjects.btn_register)



