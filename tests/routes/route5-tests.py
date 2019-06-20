from base.basepage import BasePage
import unittest
import pytest

@pytest.mark.usefixtures("developerOneTimeSetUp","setUp")
class InsightsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,developerOneTimeSetUp):
        self.bp = BasePage(self.driver)


    @pytest.mark.run(order=1)
    def test_Insights(self):
        self.bp.elementClick("//*[@id='root']/div/div/div/div/ul/li[3]/a/span", locatorType="xpath")


