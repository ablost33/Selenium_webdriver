import time
from utilities.teststatus import TestStatus
from pages.home.overview_page import OverviewPage
import unittest
import pytest


@pytest.mark.usefixtures("developerOneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,developerOneTimeSetUp):
        self.op = OverviewPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_monthlyButton(self):
        time.sleep(2)
        self.op.clickMonthlyButton()
        time.sleep(1)
        monthlyButton_result = self.op.verifyMonthlyButton()
        self.ts.markFinal("Verify if monthly button works. ",monthlyButton_result, " Monthly button DOES work! ")
        self.op.clickWeeklyButton()
        time.sleep(1)
        weeklyButton_result = self.op.verifyWeeklyButton()
        self.ts.markFinal("Verify if weekly button works. ", weeklyButton_result, " Weekly button DOES work! ")



