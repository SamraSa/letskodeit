import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "//a[text() ='HOME']"
    _all_courses = "//a[text() ='ALL COURSES']"
    _support = "//a[text() ='SUPPORT']"
    _my_courses = "//a[text() ='MY COURSES']"
    _user_settings_icon = "//div[@class='dropdown']//button"
    _sign_in = "//a[text()='Sign In']"

    def navigateToSignIn(self):
        self.elementClick(self._sign_in, locatorType="xpath")

    def navigateToAllCourses(self):
        self.elementClick(self._all_courses, locatorType="xpath")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="xpath")

    def navigateToPractice(self):
        self.elementClick(locator=self._support, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        #userSettingsElement = self.getElement(locator=self._user_settings_icon, locatorType="xpath")
        self.elementClick(element=userSettingsElement)







