from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_cell(self, v_dict: dict):
        for key, value in v_dict.items():
            selector = f'[name = "{key}"]'
            element = self.driver.find_element(By.CSS_SELECTOR, selector)  # Найти веб-элемент
            element.clear()  # Очистить поле
            element.send_keys(value)  # Ввести значение


    def click_submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        )
        self.driver.find_element(*self.submit_button).click()




