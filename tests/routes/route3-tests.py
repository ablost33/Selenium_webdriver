import time
from utilities.teststatus import TestStatus
from pages.home.overview_page import OverviewPage
from pages.home.createICP_page import currentICP
from pages.home.currentTasks_page import currentTasksPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class current_taskTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.op = OverviewPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.ci = currentICP(self.driver)
        self.ct = currentTasksPage(self.driver)

    @pytest.mark.run(order=1)
    def test_currentTasks(self):
        self.ci.createICP()
        self.ct.deleteICP()
        self.ct.editICP()
        self.ct.targeting()
        self.ct.on_off()
        self.ct.statistics()
        self.ct.messaging()

