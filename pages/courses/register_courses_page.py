import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _all_courses_link = "//a[text() = 'ALL COURSES']"
    _search_box = "//input[contains(@class,'dynamic-text')]"
    _search_course_icon = "//button[@class = 'find-course search-course']"
    _course = "//div[@class = 'col-md-12']//h4[contains(text(), '{0}')]"
    _JS_course = "//div[@class = 'col-md-12']//h4[contains(text(), 'JavaScript for beginners')]"
    _all_courses = "//div[@id = 'course-list']"
    _enroll_button = "//button[contains(@class,'dynamic-button')]"
    _cc_num = "//div[contains(@class,'CardNumberField-input-wrapper')]//input"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _country_list = "//select[@name='country-list']"
    _austria_option = "//select[@name='country-list']//option[15]"
    _buy_button = "//button[contains(@class, 'zen-subscribe')][1]"
    _enroll_error_message = "//span[text() = 'Your card was declined. Your request was in live mode, but used a known test card.']"


    ############################
    ### Element Interactions ###
    ############################

    def clickAllCoursesLink(self):
        self.elementClick(self._all_courses_link, locatorType="xpath")


    def enterCourseName(self, name):
        self.elementClick(self._search_box, locatorType="xpath")
        time.sleep(2)
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        time.sleep(5)
        self.elementClick(self._search_course_icon, locatorType="xpath")


    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")


    def clickOnEnrollButton(self):
        self.elementClick(self._enroll_button, locatorType="xpath")


    def enterCardNum(self, num):
        #dynamical iframe name
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.elementClick(self._cc_num, locatorType="xpath")
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()


    def enterCardExp(self, exp):
        # dynamical iframe name
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()


    def enterCardCVV(self, cvv):
        #dynamical iframe name
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()


    def selectCountry(self):
        self.elementClick(self._country_list, locatorType="xpath")
        self.elementClick(self._austria_option, locatorType="xpath")


    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.selectCountry()


    def clickBuyButton(self):
        self.elementClick(self._buy_button, locatorType="xpath")


    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickBuyButton()


    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement, locatorType="xpath")
        return result