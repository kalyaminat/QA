from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

credentials = {}

class MainShop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def get_authentication(self, driver, credentials):
        for key, value in credentials.items():
            info = f'{value}'
            auth_name = self.driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys(info)
            auth_value = self.driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(info)
            self.driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()





