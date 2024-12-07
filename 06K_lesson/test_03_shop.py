import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.support import expected_conditions as EC

def test():
    driver.implicitly_wait(40)

    driver.get("https://www.saucedemo.com/")
    auth_name = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
    auth_name.send_keys("standard_user")
    auth_pass = driver.find_element(By.CSS_SELECTOR, 'input#password')
    auth_pass.send_keys('secret_sauce')
    login_button = driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()

    btn_backpack = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    btn_t_sh = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    btn_onesie = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    cont = driver.find_element(By.CSS_SELECTOR,'a.shopping_cart_link' ).click()
    check_btn = driver.find_element(By.CSS_SELECTOR, 'button#checkout').click()

    first_name = driver.find_element(By.CSS_SELECTOR, 'input#first-name')
    first_name.send_keys('Tatiana')
    last_name = driver.find_element(By.CSS_SELECTOR, 'input#last-name')
    last_name.send_keys('Kalyamina')
    p_code = driver.find_element(By.CSS_SELECTOR, 'input#postal-code')
    p_code.send_keys('196233')
    btn_cont = driver.find_element(By.CSS_SELECTOR,'input#continue').click()

    total = driver.find_element(By.CSS_SELECTOR,'div.summary_total_label').text
    print(total)
    assert total == "Total: $58.29"



