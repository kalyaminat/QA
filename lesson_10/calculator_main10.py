from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalculatorMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Ввести время ожидания")
    def send_delay(self, waiter: str):
        delay = self.driver.find_element(By.CSS_SELECTOR, 'input#delay')
        delay.clear()
        delay.send_keys(waiter)

    @allure.step("Выполнить операцию сложения")
    def get_operations(self, operations: list):
        for op in operations:
            self.driver.find_element(By.XPATH, f"//span[text()='{op}']").click()

    @allure.step("Дождаться появления результата")
    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        result = self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        return result


