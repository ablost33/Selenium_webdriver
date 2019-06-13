from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _login_class = "auth0-lock-submit"
    _email_xpath = "//input[@name='email']"
    _password_xpath = "//input[@name='password']"


    def typeEmail(self,email):
        self.sendKeys(email,self._email_xpath,locatorType="xpath")

    def typePassword(self,password):
        self.sendKeys(password,self._password_xpath,locatorType="xpath")

    def clickLoginLink(self):
        self.elementClick(self._login_class,locatorType="classname")

    def login(self, email, password):
        self.typeEmail(email)
        self.typePassword(password)
        self.clickLoginLink()


