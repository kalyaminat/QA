import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test(driver):
    driver.get("https://www.saucedemo.com/")

    credentials = {
        "username": "standard_user",
        "password": "secret_sauce"
    }

    auth_name = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
    auth_name.send_keys("standard_user")
    auth_pass = driver.find_element(By.CSS_SELECTOR, 'input#password')
    auth_pass.send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()

    products = [
        '#add-to-cart-sauce-labs-backpack',
        '#add-to-cart-sauce-labs-bolt-t-shirt',
        '#add-to-cart-sauce-labs-onesie'
    ]
    for product in products:
        driver.find_element(By.CSS_SELECTOR, product).click()


    driver.find_element(By.CSS_SELECTOR,'a.shopping_cart_link' ).click()
    driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()

    driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('Tatiana')
    driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys('Kalyamina')
    driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys('196233')
    driver.find_element(By.CSS_SELECTOR,'input#continue').click()

    total = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label'))
    ).text

    assert total == "Total: $58.29"



