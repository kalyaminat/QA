import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from main_shop import MainShop

products = []

class Goods:
    def __init__(self, driver):
        self.driver = driver

    def buy_goods(self, driver):
        for product in products:
            self.driver.find_element(By.CSS_SELECTOR, product).click()

    def go_to_cart(self, driver):
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

