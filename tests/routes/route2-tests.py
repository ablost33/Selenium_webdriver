import time
from utilities.teststatus import TestStatus
from base.basepage import BasePage
from pages.home.createICP_page import currentICP
from pages.home.templateEmails_page import templateEmails
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.op = currentICP(self.driver)
        self.ts = TestStatus(self.driver)
        self.bp = BasePage(self.driver)
        self.te = templateEmails(self.driver)

    @pytest.mark.run(order=1)
    def test_createICP(self):
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

