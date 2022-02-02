import unittest
import pytest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("spacetest0411@gmail.com", "test123")
        result1 = self.lp.verifyTitle()
        #assert result1 == True
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("spacetest0411@gmail.com", "test12")
        result = self.lp.verifyLoginFailed()
        assert result == True

