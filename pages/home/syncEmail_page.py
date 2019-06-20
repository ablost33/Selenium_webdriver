from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import time
import logging
from base.basepage import BasePage


class syncEmail(BasePage):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    _syncEmailIcon_xpath ="//*[@id='root']/div/div/div/div/ul/li[5]/a"
    _syncEmailButton_xpath = "//*[@id='root']/div/div/main/div/div/button"
    _enterEmailButton_xpath = "//*[@id='login_hint']"

    def setupSync(self):
        self.elementClick(self._syncEmailIcon_xpath,locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._syncEmailButton_xpath, locatorType="xpath")
        time.sleep(3)

    def setupSync2(self):
        self.elementClick(self._enterEmailButton_xpath, locatorType="xpath")
        time.sleep(2)
        self.sendKeys("sadasda", self._enterEmailButton_xpath, locatorType="xpath")


