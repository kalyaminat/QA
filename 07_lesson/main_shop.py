from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


#credentials = {}

class MainShop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def wait(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "input#user-name")))

    def complete_authentication(self,credentials):
        for key, value in credentials.items():
            auth_name = self.driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys(credentials["username"])
            auth_value = self.driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(credentials["password"])
            self.driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()





