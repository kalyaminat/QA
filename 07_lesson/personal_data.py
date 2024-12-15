import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from main_shop import MainShop

personal = dict()

class PersonalData:
    def __init__(self, driver):
        self.driver = driver

    def fill_personal_data(self, driver):
        for key, value in personal.items():
            data = f'{value}'
            first_name = self.driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys(data)
            last_name = self.driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys(data)
            postal_code = self.driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys(data)
            driver.find_element(By.CSS_SELECTOR, 'input#continue').click()



