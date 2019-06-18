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
    _exitButton_class = "//*[@id='intercom-container']/div/div"

    def removeIntercomChat(self):

        element = self.getElement(self._intercomChat_xpath,locatorType="xpath")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.elementClick(self._intercomChat_xpath,locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._exitButton_class,locatorType="xpath")






