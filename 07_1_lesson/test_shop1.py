from selenium.webdriver.chrome.webdriver import WebDriver
from main_shop1 import *

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


def test_shopping(browser: WebDriver):

    authorization = Authorization(browser)
    authorization.fill_parameters('user-name', "standard_user")
    authorization.fill_parameters('password', "secret_sauce")
    authorization.login()

    catalog = Catalog(browser)
    catalog.add_to_cart('add-to-cart-sauce-labs-backpack')
    catalog.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    catalog.add_to_cart('add-to-cart-sauce-labs-onesie')

    cart = Cart(browser)
    cart.click_checkout()
    cart.input_infirmation('first-name', "Tatiana")
    cart.input_infirmation('last-name', "Kalyamina")
    cart.input_infirmation('postal-code', "196233")
    cart.go_ahead()

    assert '58.29' in cart.find_total()