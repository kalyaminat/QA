import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from main_shop import MainShop
from goods import Goods
from cart_page import Cart
from personal_data import PersonalData
from check_total import CheckTotal

credentials = {
    "username": "standard_user",
    "password": "secret_sauce"
}
personal = {
    "first_name": "Tatiana",
    "last_name": "Kalyamina",
    "postal_code": "196233"
}
products = [
        '#add-to-cart-sauce-labs-backpack',
        '#add-to-cart-sauce-labs-bolt-t-shirt',
        '#add-to-cart-sauce-labs-onesie'
    ]

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()

def test_cart(driver):
    main_shop = MainShop(driver)
    main_shop.get_authentication()

    goods = Goods(driver)
    goods.buy_goods()
    goods.go_to_cart()

    cart = Cart(driver)
    cart.checkout()

    personal_data = PersonalData(driver)
    personal_data.fill_personal_data()

    check_total = CheckTotal(driver)
    check_total.check_total()

    assert check_total.check_total().text == "Total: $58.29"





