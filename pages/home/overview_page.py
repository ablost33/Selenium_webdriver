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

    _monthlybutton_class = "route-home_label__1YGkr"
    _contactedbutton_xpath = "//input[@id='tour_campaign_performance']"

    def clickMonthlyButton(self):
        self.elementClick(self._monthlybutton_class,locatorType="classname")

    def verifyMonthlyButton(self):
        textString =  self.getText(locator=self._contactedbutton_xpath, locatorType="xpath")
        if Util.verifyTextContains(textString,"Monthly"):
            return True
        else:
            return False


