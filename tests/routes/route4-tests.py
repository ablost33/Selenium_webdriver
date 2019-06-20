import time
from utilities.teststatus import TestStatus
from base.basepage import BasePage
from pages.home.prospects import ProspectsPage
import unittest
import pytest

@pytest.mark.usefixtures("developerOneTimeSetUp","setUp")
class ProspectsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,developerOneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.bp = BasePage(self.driver)
        self.p = ProspectsPage(self.driver)


    @pytest.mark.run(order=1)
    def test_Prospects(self):
        self.p.openProspects()


