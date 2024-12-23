from selenium.webdriver.common.by import By


class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(" https://www.saucedemo.com/")

# Вессти логин
    def fill_parameters(self, element, value):
        self.driver.find_element(By.ID, element).send_keys(value)

# Ввести пароль
    #def password(self, element, value):
    #    self.driver.find_element(By.ID, element).send_keys(value)

# Подтвердить
    def login(self):
        self.driver.find_element(By.ID, 'login-button').click()

from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/cart.html')

# Нажать checkout
    def click_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

# Заполнить информацию о покупателе
    def input_infirmation(self, element, value):
        self.driver.find_element(By.ID, element).send_keys(value)

# Нажать далее
    def go_ahead(self):
        self.driver.find_element(By.ID, 'continue').click()

# Получить сумму покупок
    def find_total(self):
        return self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text.replace('Total: $', '')

from selenium.webdriver.common.by import By


class Catalog:

    def __init__(self, driver):
        self.driver = driver

# Положить товары в корзину
    def add_to_cart(self, element):
        self.driver.find_element(By.ID, element).click()