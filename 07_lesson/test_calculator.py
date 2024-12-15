import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from calculator_main import CalculatorMainPage

operations = ['7', '+', '8', '=']
expected = '15'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_assertion(driver):
    main_page = CalculatorMainPage(driver)
    main_page.send_delay()
    main_page.get_operations()
    main_page.get_result()

    assert main_page.get_result().text == expected


