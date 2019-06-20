from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class ProspectsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    _prospectsButton_xpath = "//*[@id='root']/div/div/div/div/ul/li[2]/a/span"
    _ubicoContacts_xpath = "//*[@id='io.ubico.CONTACTS']"
    _importFromCRM_xpath = "//*[@id='io.ubico.IMPORT_DYNAMICS']"


    def openProspects(self):
        self.elementClick(self._prospectsButton_xpath, locatorType="xpath")
        self.elementClick(self._ubicoContacts_xpath, locatorType="xpath")
        self.elementClick(self._importFromCRM_xpath, locatorType="xpath")
