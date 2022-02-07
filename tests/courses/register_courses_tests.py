import unittest
import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()


    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        #self.courses.clickAllCoursesLink()
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="5105 1051 0510 5100", exp="1223", cvv="102")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")



