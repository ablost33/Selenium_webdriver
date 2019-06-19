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

    _weeklybutton_xpath = "//*[@id='tour_campaign_performance']/div/ul/li[1]"
    _monthlybutton_xpath= "//*[@id='tour_campaign_performance']/div/ul/li[2]/div"
    _contactedbutton_xpath = "//*[@id='tour_campaign_performance']/ul/div[2]/div[1]"


    def clickMonthlyButton(self):
        self.elementClick(self._monthlybutton_xpath,locatorType="xpath")

    def clickWeeklyButton(self):
        self.elementClick(self._weeklybutton_xpath, locatorType="xpath")

    def verifyMonthlyButton(self):
        textString =  self.getText(locator=self._contactedbutton_xpath, locatorType="xpath")
        self.log.info("                                                   ")
        self.log.info(" ---------- BEGIN TESTING MONTHLY BUTTON ----------")
        if self.util.verifyTextContains(textString, "month"):
            return True
        else:
            return False

    def verifyWeeklyButton(self):
        textString = self.getText(locator=self._contactedbutton_xpath, locatorType="xpath")
        self.log.info("                                                   ")
        self.log.info(" ---------- BEGIN TESTING WEEKLY BUTTON ----------")
        if self.util.verifyTextContains(textString, "week"):
            return True
        else:
            return False



