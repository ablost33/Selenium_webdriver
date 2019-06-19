from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
from selenium.webdriver import ActionChains
import time


class BasePage(SeleniumDriver):

    def __init__(self,driver):
        super(BasePage,self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    _intercomChat_xpath = "//*[@id='intercom-container']/div/iframe"
    _exitButton_class = "//*[@id='intercom-container']/div/div/div[2]"
    _next1_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div/div[2]/button"

    def removeIntercomChat(self):

        openIntercomButton = self.getElement(self._intercomChat_xpath,locatorType="xpath")
        actions = ActionChains(self.driver)
        actions.move_to_element(openIntercomButton).perform()
        self.elementClick(self._intercomChat_xpath,locatorType="xpath")
        time.sleep(1)

        closeIntercomButton = self.getElement(self._intercomChat_xpath,locatorType="xpath")
        actions = ActionChains(self.driver)
        actions.move_to_element(closeIntercomButton).perform()
        self.elementClick(self._intercomChat_xpath,locatorType="xpath")

        next1button = self.getElement(self._next1_xpath, locatorType="xpath")
        actions = ActionChains(self.driver)
        actions.move_to_element(next1button).perform()
        self.elementClick(self._next1_xpath,locatorType="xpath")






