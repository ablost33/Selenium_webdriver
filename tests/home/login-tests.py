from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://insights.ubico.io/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login("test@ubico.io", "Ubico")
        time.sleep(3)

        if "Ubico" == driver.title:
            print("Login Successful")
        else:
            print("Login Failed")
        driver.quit()
