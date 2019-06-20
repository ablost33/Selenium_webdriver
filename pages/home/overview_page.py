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
    _assistantName_xpath = "//*[@id='assistantName']/div/div[1]"
    _assistantTitle_xpath = "//*[@id='assistantTitle']/div/div[1]"
    _frequencyreports_xpath = "//*[@id='root']/div/div/main/div/div[1]/div[2]/input"
    _createButton_xpath = "//*[@id='root']/div/div/main/div/div[1]/div[2]/div[3]"


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

    def buildAssistant(self):

        self.elementClick(self._assistantName_xpath,locatorType="xpath")
        self.elementClick("div.css-15k3avv",locatorType="css")

        self.elementClick(self._assistantTitle_xpath, locatorType="xpath")
        self.elementClick("div.css-15k3avv",locatorType="css")

        self.elementClick(self._frequencyreports_xpath, locatorType="xpath")
        self.sendKeys("5", self._frequencyreports_xpath, locatorType="xpath")
        self.elementClick(self._createButton_xpath, locatorType="xpath")






