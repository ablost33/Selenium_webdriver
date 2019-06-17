import time
from utilities.teststatus import TestStatus
from pages.home.overview_page import OverviewPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.op = OverviewPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_monthlyButton(self):
        time.sleep(2)
        self.op.clickMonthlyButton()
        time.sleep(1)
        self.op.verifyMonthlyButton()
