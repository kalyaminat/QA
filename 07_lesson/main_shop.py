from selenium.webdriver.common.by import By
import pytest
from webdriver_manager.core import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

#credentials = {}

class MainShop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")


    def complete_authentication(self,credentials):
        for key, value in credentials.items():
            self.driver.find_element(By.CSS_SELECTOR, 'input#user-name').click()
            self.driver.send_keys(credentials["username"])
            self.driver.find_element(By.CSS_SELECTOR, 'input#password').click()
            self.driver.send_keys(credentials["password"])
            self.driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()





