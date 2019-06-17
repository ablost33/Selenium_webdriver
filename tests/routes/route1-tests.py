import time
from utilities.teststatus import TestStatus
from pages.home.overview_page import OverviewPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = OverviewPage(self.driver)
        self.ts = TestStatus(self.driver)
