from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util
import time

class templateEmails(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _recentNews_xpath = "//*[@id='recentNews']/span[1]"
    _recentContent_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[2]/span[1]"
    _15minutes_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[3]/span[1]"
    _10xTraction_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[4]/span[1]"
    _weather_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[5]/span[1]"
    _clientTestimonial_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[6]/span[1]"
    _followUp_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[7]/span[1]"
    _productExample_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[8]/span[1]"
    _resetButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button[9]/span[1]"
    _subject_xpath ="//*[@id='io.ubico.emailSubject']"
    _email_xpath = "//*[@id='io.ubico.text']/div[2]/div[1]"
    _saveButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/button[1]"
    _bigBottomNextButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[4]/div[4]/button[1]/span[1]"
    _finishButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[4]/div[4]/button[1]/span[1]"

    def clickAllTemplates(self):
        self.elementClick(self._recentNews_xpath, locatorType="xpath")
        self.elementClick(self._recentContent_xpath, locatorType="xpath")
        self.elementClick(self._15minutes_xpath, locatorType="xpath")
        self.elementClick(self._10xTraction_xpath, locatorType="xpath")
        self.elementClick(self._weather_xpath, locatorType="xpath")
        self.elementClick(self._clientTestimonial_xpath, locatorType="xpath")
        self.elementClick(self._followUp_xpath, locatorType="xpath")
        self.elementClick(self._productExample_xpath, locatorType="xpath")
        self.elementClick(self._resetButton_xpath,locatorType="xpath")

    def typeRandomEmail(self):
        subject = self.util.getAlphaNumeric(20)
        email = self.util.getAlphaNumeric(200)
        self.sendKeys(subject,self._subject_xpath,locatorType="xpath")
        self.sendKeys(email,self._email_xpath,locatorType="xpath")
        self.elementClick(self._saveButton_xpath,locatorType="xpath")


    def typeEmailNoSubject(self):
        email = self.util.getAlphaNumeric(200)
        self.sendKeys(email,self._email_xpath,locatorType="xpath")
        self.elementClick(self._saveButton_xpath,locatorType="xpath")


    def typeTemplateEmail(self):
        self.elementClick(self._10xTraction_xpath, locatorType="xpath")
        self.elementClick(self._saveButton_xpath,locatorType="xpath")

    def checkTemplateEmail(self):
        self.log.info("About to run template email test")
        text = self.getText(self._10xTraction_xpath, locatorType="xpath")
        return self.util.verifyTextContains(text,"10x {Company}'s traction in 10 minutes")

    def finishCampaignCreation(self):
        self.elementClick(self._bigBottomNextButton_xpath,locatorType="xpath")
        input("waiting on you:")
        self.elementClick(self._finishButton_xpath,locatorType="xpath")




