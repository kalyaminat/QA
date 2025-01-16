from selenium.webdriver.chrome.webdriver import WebDriver
from main_shop10 import *

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

@allure.title("Интернет-магазин")
@allure.description("Зарегистрироваться, положить товары в корзину, ввести личные данные, проверить итоговую сумму")
@allure.severity("blocker")
def test_shopping(browser: WebDriver):

    with allure.step("Создание экземпляра класса Authorization"):
        authorization = Authorization(browser)
    with allure.step("Ввод логина"):
        authorization.fill_parameters('user-name', "standard_user")
    with allure.step("Ввод пароля"):
        authorization.fill_parameters('password', "secret_sauce")
    with allure.step("Подтверждение"):
        authorization.login()

    with allure.step("Создание экземпляра класса Catalog"):
        catalog = Catalog(browser)
    with allure.step("Первый товар в корзину"):
        catalog.add_to_cart('add-to-cart-sauce-labs-backpack')
    with allure.step("Второй товар в корзину"):
        catalog.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    with allure.step("Третий товар в корзину"):
        catalog.add_to_cart('add-to-cart-sauce-labs-onesie')

    with allure.step("Создание экземпляра класса Cart"):
        cart = Cart(browser)
    with allure.step("Нажать checkout, переход в форму с личными данными"):
        cart.click_checkout()
    with allure.step("Ввод имени"):
        cart.input_information('first-name', "Tatiana")
    with allure.step("Ввод фамилии"):
        cart.input_information('last-name', "Kalyamina")
    with allure.step("Ввод индекса"):
        cart.input_information('postal-code', "196233")
    with allure.step("Нажать Continue, переход к просмотру корзины"):
        cart.go_ahead()

    with allure.step("Проверка суммы покупок"):
        assert '58.29' in cart.find_total()