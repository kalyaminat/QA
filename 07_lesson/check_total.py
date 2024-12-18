import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_shop import MainShop

class CheckTotal:
    def __init__(self, driver):
        self.driver = driver

    def check_total(self, driver):
        total = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label'))
        ).text
