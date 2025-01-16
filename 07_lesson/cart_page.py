import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from main_shop import MainShop

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self, driver):
        self.driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()