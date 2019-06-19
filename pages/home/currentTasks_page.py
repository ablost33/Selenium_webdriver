from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from pages.home.createICP_page import currentICP

class currentTasksPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.ci = currentICP(self.driver)

    _trashCanButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[2]/div[1]/span[2]"
    _deleteButton_xpath = "//*[@id='root']/div/div/main/div/div/div[3]/div[2]/div/div/button[1]"
    _pencilButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[2]/div[2]/span[1]"
    _bigTargetIcon_xpath ="//*[@id='StepOneTargeting']"
    _editStep_xpath = "//*[@id='root']/div/div/main/div/div/div/div[3]/button"
    _updateTargeting_xpath = "//*[@id='root']/div/div/main/div/div/div/div/div[2]/button[2]"
    _smallTargetIcon_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[2]/div[1]/div[2]/span[2]"
    _targetExitIcon_xpath = "//*[@id='root']/div/div/main/div/div/div[1]/div[2]/span/img"
    _onOffSwitch_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[2]/div[1]/label/span[1]/span[1]"
    _messageIcon_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[2]/div[1]/div[2]/span[3]"
    _statisticsIcon_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[2]/div[1]/div[2]/span[1]"


    def deleteICP(self):
        self.elementClick(self._trashCanButton_xpath, locatorType="xpath")
        self.elementClick(self._deleteButton_xpath, locatorType="xpath")


    def editICP(self):
        time.sleep(5)
        self.elementClick(self._pencilButton_xpath, locatorType="xpath")
        self.elementClick(self._bigTargetIcon_xpath, locatorType="xpath")
        self.elementClick(self._editStep_xpath, locatorType="xpath")
        self.ci.fillListName()
        self.elementClick("//*[@id='root']/div/div/main/div/div/div/div/div[2]/button", locatorType="xpath")
        self.elementClick("//*[@id='root']/div/div/main/div/div/div/div/div[2]/button[2]", locatorType="xpath")
        self.ci.addJobTitle()
        self.elementClick(self._updateTargeting_xpath, locatorType="xpath")

    def targeting(self):
        time.sleep(5)
        self.elementClick(self._smallTargetIcon_xpath, locatorType="xpath")
        self.elementClick(self._targetExitIcon_xpath, locatorType="xpath")

    def on_off(self):
            # here maybe try clicking on all of the button elements
            self.elementClick(self._onOffSwitch_xpath, locatorType="xpath")

    def messaging(self):
        time.sleep(5)
        self.elementClick(self._messageIcon_xpath, locatorType="xpath")
        self.elementClick(self._targetExitIcon_xpath, locatorType="xpath")

    def statistics(self):
        time.sleep(5)
        self.elementClick(self._statisticsIcon_xpath, locatorType="xpath")
        time.sleep(3)
        self.elementClick(self._targetExitIcon_xpath, locatorType="xpath")


