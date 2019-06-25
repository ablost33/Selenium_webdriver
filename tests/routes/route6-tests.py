import time
from utilities.teststatus import TestStatus
from base.basepage import BasePage
from pages.home.syncEmail_page import syncEmail
import unittest
import pytest

@pytest.mark.usefixtures("developerOneTimeSetUp","setUp")
class syncEmailTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,developerOneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.bp = BasePage(self.driver)
        self.se = syncEmail(self.driver)


    @pytest.mark.run(order=1)
    def test_emailSync(self):
        self.se.setupSync()
