from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("est@ubico.io", "bico2018")
        time.sleep(3)
        result = self.lp.verifyLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        time.sleep(3)
        self.lp.login("t","U")
        time.sleep(3)
        result = self.lp.verifyLoginSuccessful()
        assert result == False



