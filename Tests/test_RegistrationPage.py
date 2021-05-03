import pytest
from Library import *
from POM import RegisterationPage

headers = ["fname", "lname", "email", "password"]
data = [("Mekala", "Manikanta", "manikantac779@gmail.com", "Mani@098")]


@pytest.mark.usefixtures("init")
class TestRegistrationPage:

    @pytest.mark.parametrize(headers, data)
    def test_registration(self, fname, lname, email, password):
        rp = RegisterationPage.RegisterationPage(self.driver, fname, lname, email, password) #doubt
        rp.Register_link()
        rp.click_female_radio_button()
        rp.enter_firstname()
        rp.enter_lastname()
        rp.enter_email()
        rp.enter_password()
        rp.confirm_password()
