from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.basepage import BasePage
from utilities.util import Util
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


class currentTasksPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _createIcon_xpath = "//*[@id='root']/div/div/main/div/a/span"
    _createNewCampaign_xpath = "//*[@id='root']/div/div/main/div/div/div[1]/div/div[2]"
    _ICPname_ID = "io.ubico.ICP_NAME"
    _ICPdescription_ID = "io.ubico.IDEAL_LEADS"
    _next1_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div/div[2]/button"
    _createNewButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div/button/span[1]"
    _countryCriteria_ID = "io.ubico.TARGET_COUNTRIES"
    _cityCriteria_ID = "io.ubico.TARGET_CITIES"
    _industryCriteria_ID = "io.ubico.TARGET_INDUSTRIES"
    _employCount_ID = "io.ubico.EMPLOYEES_COUNT"
    _bottomNextButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[4]/div[4]/button/span[1]"
    _addCampaignStep_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div/button/span[1]"
    _createNewStep_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div"


    def fillListName(self):
        self.elementClick(self._createIcon_xpath,locatorType="xpath")
        self.elementClick(self._createNewButton_xpath, locatorType="xpath")
        name = self.util.getUniqueName()
        self.sendKeys(name,self._ICPname_ID)
        text = self.util.getAlphaNumeric(250)
        self.sendKeys(text,self._ICPdescription_ID)
        self.elementClick(self._bottomNextButton_xpath,locatorType="xpath")

    def addCampaignStep(self):
        self.elementClick(self._addCampaignStep_xpath,locatorType="xpath")

    def fillCountryCriteria(self):

        self.elementClick(self._next1_xpath, locatorType="xpath")

        element = self.getElement(self._countryCriteria_ID)
        sel = Select(element)
        sel.select_by_value("Canada")

        element = self.getElement(self._cityCriteria_ID)
        sel = Select(element)
        sel.select_by_value("Ontario, ON, Canada")

        element = self.getElement(self._industryCriteria_ID)
        sel = Select(element)
        sel.select_by_value("Advertising-Computer")

        element = self.getElement(self._industryCriteria_ID)
        sel = Select(element)
        sel.select_by_value("1-10")

    def createNewStep(self):
        self.elementClick(self._createNewStep_xpath, locatorType="xpath")








# def makeCustomCriteria
