import pytest
import time
from Library import *
from POM import loginpage

headers = ["email", "password"]
data=[("manikantac779@gmail.com", "Mani@098"), ("mmekala098@gmail.com", "Mani@098")]

@pytest.mark.usefixtures("init")
class TestLoginPage:

    @pytest.mark.parametrize(headers, data)
    def test_login(self,email, password):
        lp= loginpage.LoginPage(self.driver,email,password)
        time.sleep(2)
        lp.login_link()
        time.sleep(2)
        lp.enter_email()
        time.sleep(2)
        lp.enter_password()
        time.sleep(2)
        lp.submit_login()
        time.sleep(2)
        lp.logut_page()
        time.sleep(2)
        lp.login_link()


