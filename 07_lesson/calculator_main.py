from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def send_delay(self, driver, operation):
        delay = self.driver.find_element(By.CSS_SELECTOR, 'input#delay')
        delay.clear()
        delay.send_keys('operation')

    def get_operations(self, driver):
        operations = list()
        for op in operations:
            self.driver.find_element(By.XPATH, f"//span[text()='{op}']").click()

    def get_result(self, driver, result):
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "result"))
        result = self.driver.find_element(By.CSS_SELECTOR, '.screen').text


