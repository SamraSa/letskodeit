from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
import logging
import  utilities.custom_logger as cl

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _signIn_link = "//a[text() = 'Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//div[@class = 'col-xs-12 col-md-12']//input"


    def clickLoginLink(self):
        self.elementClick(self._signIn_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@class='dropdown']",
                                       locatorType="xpath")

        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid.')]",
                                       locatorType="xpath")

        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyTitle(self):
        if "Google" in self.getTitle():
            return True
        else:
            return False


