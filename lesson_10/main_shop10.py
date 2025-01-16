from selenium.webdriver.common.by import By
import allure

class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(" https://www.saucedemo.com/")

    @allure.step("Ввести логин и пароль")
    def fill_parameters(self, element: str, value: str):
        self.driver.find_element(By.ID, element).send_keys(value)

    @allure.step("Подтвердить")
    def login(self):
        self.driver.find_element(By.ID, 'login-button').click()


class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/cart.html')

    @allure.step("Нажать checkout")
    def click_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

    @allure.step("Заполнить информацию о покупателе")
    def input_information(self, element: str, value: str):
        self.driver.find_element(By.ID, element).send_keys(value)

    @allure.step("Нажать далее")
    def go_ahead(self):
        self.driver.find_element(By.ID, 'continue').click()

    @allure.step("Получить сумму покупок")
    def find_total(self):
        return self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text.replace('Total: $', '')

from selenium.webdriver.common.by import By


class Catalog:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Положить товары в корзину")
    def add_to_cart(self, element: str):
        self.driver.find_element(By.ID, element).click()