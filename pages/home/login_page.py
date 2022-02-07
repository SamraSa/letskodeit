
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _signIn_link = "//a[text() = 'Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//div[@class = 'col-xs-12 col-md-12']//input"
    _logout = "//a[text()='Logout']"
    _settings_button = "//button[@id='dropdownMenu1']"

    def clickLoginLink(self):
        self.elementClick(self._signIn_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def clickSettingsIcon(self):
        self.getElement(locator="//div[@class='dropdown']//button", locatorType="xpath")
        self.elementClick(
            locator="//div[@class='dropdown']//button", locatorType="xpath"
        )

    def logout(self):
        self.nav.navigateToUserSettings()
        self.elementClick(locator="//a[text()='Logout']", locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@class='dropdown']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(
            "//span[contains(text(),'Your username or password is invalid.')]",
            locatorType="xpath",
        )
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyTitle(self):
        if "My Courses" in self.getTitle():
            return True
        else:
            return False

    def clickOnIcon(self):
        self.getElement(locator="//a[text() ='MY COURSES']", locatorType="xpath")
        self.elementClick(locator="//a[text() ='MY COURSES']", locatorType="xpath")
