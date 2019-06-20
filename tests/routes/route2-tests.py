import time
from utilities.teststatus import TestStatus
from base.basepage import BasePage
from pages.home.createICP_page import currentICP
from pages.home.templateEmails_page import templateEmails
from pages.home.overview_page import OverviewPage
import unittest
import pytest


@pytest.mark.usefixtures("developerOneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):
    answer = input("Are you testing on localhost?(y/n)  ")

    if answer == "y":
        @pytest.fixture(autouse=True)
        def classSetup(self,developerOneTimeSetUp):
            self.op = currentICP(self.driver)
            self.ts = TestStatus(self.driver)
            self.bp = BasePage(self.driver)
            self.te = templateEmails(self.driver)
            self.ov = OverviewPage(self.driver)



    elif answer == "n":
        @pytest.fixture(autouse=True)
        def classSetup(self,oneTimeSetUp):
            self.op = currentICP(self.driver)
            self.ts = TestStatus(self.driver)
            self.bp = BasePage(self.driver)
            self.te = templateEmails(self.driver)
            self.ov = OverviewPage(self.driver)

    @pytest.mark.run(order=1)
    def test_createICP(self):
        # self.ov.buildAssistant()
        self.op.fillListName()
        self.op.fillCountryCriteria()
        self.op.makeCustomCriteria()
        self.op.addCampaignStep()
        self.te.clickAllTemplates()
        self.te.typeRandomEmail()
        self.op.createNewStep()
        self.te.typeRandomEmail()
        self.op.createNewStep()
        self.te.typeEmailNoSubject()
        self.ts.webScroll(direction="down")
        self.op.createNewStep()
        self.te.typeTemplateEmail()
        self.te.finishCampaignCreation()

