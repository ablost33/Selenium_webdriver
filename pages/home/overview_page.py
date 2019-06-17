from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util

class OverviewPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _monthlybutton_xpath= "//*[@id='tour_campaign_performance']/div/ul/li[2]/div"
    _contactedbutton_xpath = "//*[@id='tour_campaign_performance']/ul/div[2]/div[1]"

    def clickMonthlyButton(self):
        self.elementClick(self._monthlybutton_xpath,locatorType="xpath")

    def verifyMonthlyButton(self):
        textString =  self.getText(locator=self._contactedbutton_xpath, locatorType="xpath")
        textString2 = "month"
        if self.util.verifyTextContains(textString, "month"):
            return True
        else:
            return False


