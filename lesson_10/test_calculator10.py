import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from calculator_main10 import CalculatorMainPage
import allure

waiter = '45'
operations = ['7', '+', '8', '=']
expected = '15'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

@allure.title("Тест калькулятора")
@allure.description("Тест калькулятора с длительной отсрочкой выполнения операции")
@allure.severity("normal")
def test_assertion(driver):
    with allure.step("Создание экземпляра класса"):
        main_page = CalculatorMainPage(driver)
    with allure.step("Ввод времени ожидания"):
        main_page.send_delay(waiter)
    with allure.step("Выполнить операцию сложения"):
        main_page.get_operations(operations)
    with allure.step("Дождаться появления результата"):
        main_page.get_result()

    with allure.step("Убедиться, что полученный результат равен ожидаемому"):
        assert main_page.get_result() == expected


