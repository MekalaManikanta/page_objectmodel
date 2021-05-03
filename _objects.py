class BasePageObjects:

    lnk_register = ("link text", "Register")
    lnk_login = ("xpath", "//a[text()='Log in']")
    txt_search_store = ("name", "q")
    lnk_logout = ("xpath", "//a[text()='Log out']")
    lnk_shopping_cart = ("xpath", "//span[text()='Shopping cart']")
    lnk_books = ("xpath", "(//a[contains(text(), 'Books')])[3]")
    lnk_email = ("xpath", "//a[text()='{}']")
    btn_add_cart = ("xpath", "//a[text()='{}']/../..//input[@value='Add to cart']")


class RegistrationPageObjects:

    rdo_male = ("id", "gender-male")
    rdo_female = ("id", "gender-female")
    txt_firstname = ("name", "FirstName")
    txt_lastname = ("name", "LastName")
    txt_email = ("id", "Email")
    txt_password = ("name", "Password")
    txt_confirm_password = ("name", "ConfirmPassword")
    btn_register = ("name", "register-button")
    lbl_reg_success = ("xpath", "//div[contains(text(), 'Your registration completed')]")


class LoginPageObjects:
    txt_email = ("name", "Email")
    txt_password = ("name", "Password")
    btn_login = ("xpath", "//input[@value='Log in']")

