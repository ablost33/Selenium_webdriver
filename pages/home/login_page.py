from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _login_xpath = "//*[@id='root']/div/div[1]"
    _email_xpath = "//*[@id='root']/div/input[1]"
    _password_xpath = "//*[@id='root']/div/input[2]"


    def typeEmail(self,email):
        self.sendKeys(email,self._email_xpath,locatorType="xpath")

    def typePassword(self,password):
        self.sendKeys(password,self._password_xpath,locatorType="xpath")

    def clickLoginLink(self):
        self.elementClick(self._login_xpath,locatorType="xpath")

    def login(self, email="", password=""):
        self.typeEmail(email)
        self.typePassword(password)
        self.clickLoginLink()

    def verifyLoginSuccessful(self):
      return self.verifyPageTitle("Ubico")




