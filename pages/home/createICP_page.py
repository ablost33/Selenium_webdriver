from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.basepage import BasePage
from utilities.util import Util
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.home.templateEmails_page import templateEmails




class currentICP(BasePage):



    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.te = templateEmails(self.driver)




    _createIcon_xpath = "//*[@id='root']/div/div/main/div/a/span"
    _createNewCampaign_xpath = "//*[@id='root']/div/div/main/div/div/div[1]/div/div[2]"
    _ICPname_ID = "io.ubico.ICP_NAME"
    _ICPdescription_ID = "io.ubico.IDEAL_LEADS"
    _createNewButton_xpath = "//*[@id='root']/div/div/main/div/div/div[1]/div/div[2]"
    _countryCriteria_xpath = "//*[@id='io.ubico.TARGET_COUNTRIES']/div/div[1]"
    _cityCriteria_xpath = "//*[@id='io.ubico.TARGET_CITIES']/div/div[1]"
    _industryCriteria_xpath = "//*[@id='io.ubico.TARGET_INDUSTRIES']/div/div[1]"
    _employCount_xpath = "//*[@id='io.ubico.EMPLOYEES_COUNT']/div/div[1]"
    _bottomNextButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[4]/div[4]/button/span[1]"
    _littleNextButton_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div/div[3]/button[2]"
    _addCampaignStep_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div/button/span[1]"
    _createNewStep_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/div"
    _startCustomCriteria_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div/div[1]/button"
    _annualRevenue_xpath = "//*[@id='io.ubico.COMPANY_REVENUE']/div/div[1]"
    _customCriteria_xpath = "//*[@id='io.ubico.CRITERIA_DESCRIPTION']"
    _addCustomCriteria_xpath = "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div[1]/div/div[2]/div[9]/div/div[2]"
    _numberOfContacts_xpath = "//*[@id='io.ubico.COMPANY_CONTACT_COUNT']"
    _seniorityLevel_xpath = "//*[@id='io.ubico.SENIORITY_LEVEL']"
    _choosePosition_xpath = "//*[@id='io.ubico.POSITION']"
    _customJobTitle_xpath = "//*[@id='io.ubico.CUSTOM_JOB_TITLE_INPUT']"
    _addAnotherJobTitle_xpath = "//*[@id='root']/div/div/main/div/div/div/div/div[1]/div[8]/div[1]"

    def fillListName(self):
        self.elementClick(self._createIcon_xpath,locatorType="xpath")
        self.elementClick(self._createNewButton_xpath, locatorType="xpath")
        name = self.util.getUniqueName()
        self.sendKeys(name,self._ICPname_ID)
        text = self.util.getAlphaNumeric(250)
        self.sendKeys(text,self._ICPdescription_ID)


    def addCampaignStep(self):
        self.elementClick(self._addCampaignStep_xpath,locatorType="xpath")

    def fillCountryCriteria(self):

        self.webScroll(direction="down")
        self.removeIntercomChat()
        self.webScroll(direction="up")

        for x in range(3):
            self.elementClick(self._countryCriteria_xpath,locatorType="xpath")
            self.elementClick("div.css-15k3avv",locatorType="css")

        for x in range(3):
            self.elementClick(self._cityCriteria_xpath,locatorType="xpath")
            self.elementClick("div.css-15k3avv",locatorType="css")

        for x in range(2):
            self.elementClick(self._industryCriteria_xpath,locatorType="xpath")
            self.elementClick("div.css-15k3avv",locatorType="css")

        for x in range(2):
            self.elementClick(self._employCount_xpath,locatorType="xpath")
            self.elementClick("div.css-15k3avv",locatorType="css")



    def createNewStep(self):
        self.elementClick(self._createNewStep_xpath, locatorType="xpath")

    def makeCustomCriteria(self):

        self.webScroll(direction="down")
        time.sleep(1)
        self.elementClick(self._startCustomCriteria_xpath, locatorType="xpath")
        self.webScroll(direction="down")


        for x in range(2):
            self.elementClick(self._annualRevenue_xpath,locatorType="xpath")
            self.elementClick("div.css-15k3avv",locatorType="css")

        criteriaDescription = self.util.getUniqueName(10)
        self.sendKeys(criteriaDescription, self._customCriteria_xpath,locatorType="xpath")
        self.elementClick(self._addCustomCriteria_xpath,locatorType="xpath")

        self.elementClick(self._littleNextButton_xpath,locatorType="xpath")
        self.webScroll(direction="up")

        # Filling out "Let's learn about the job titles of your ideal customers"
        self.elementClick(self._numberOfContacts_xpath,locatorType="xpath")
        numberOfContacts = self.getElement(self._numberOfContacts_xpath,locatorType="xpath")
        select = Select(numberOfContacts)
        select.select_by_value("3")
        self.elementClick(self._numberOfContacts_xpath,locatorType="xpath")
        self.webScroll(direction="down")

        #Filling out target customer profile
        self.elementClick(self._seniorityLevel_xpath,locatorType="xpath")
        seniorityLevel = self.getElement(self._seniorityLevel_xpath,locatorType="xpath")
        seniorityLevelSelector = Select(seniorityLevel)
        seniorityLevelSelector.select_by_value("VP")

        self.elementClick(self._choosePosition_xpath,locatorType="xpath")
        position = self.getElement(self._choosePosition_xpath,locatorType="xpath")
        positionSelector = Select(position)
        positionSelector.select_by_value("Education")

        #Adding custom job title

        self.elementClick(self._customJobTitle_xpath,locatorType="xpath")
        customJobTitle = self.util.getUniqueName(10)
        self.sendKeys(customJobTitle, self._customJobTitle_xpath,locatorType="xpath")
        self.elementClick(self._bottomNextButton_xpath,locatorType="xpath")

    def addJobTitle(self):
        self.elementClick(self._addAnotherJobTitle_xpath, locatorType="xpath")

        self.elementClick(self._seniorityLevel_xpath,locatorType="xpath")
        seniorityLevel = self.getElement(self._seniorityLevel_xpath,locatorType="xpath")
        seniorityLevelSelector = Select(seniorityLevel)
        seniorityLevelSelector.select_by_value("Manager")

        self.elementClick(self._choosePosition_xpath,locatorType="xpath")
        position = self.getElement(self._choosePosition_xpath,locatorType="xpath")
        positionSelector = Select(position)
        positionSelector.select_by_value("Administrative")


    def createICP(self):
        self.fillListName()
        self.fillCountryCriteria()
        self.makeCustomCriteria()
        self.addCampaignStep()
        self.te.clickAllTemplates()
        self.te.typeRandomEmail()
        self.createNewStep()
        self.te.typeRandomEmail()
        self.createNewStep()
        self.te.typeEmailNoSubject()
        self.webScroll(direction="down")
        self.createNewStep()
        self.te.typeTemplateEmail()
        self.te.finishCampaignCreation()
        self.elementClick("//*[@id='root']/div/div/main/div/div/div[1]/div[2]/span/img",locatorType="xpath")














