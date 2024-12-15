from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_cell(self, v_dict: dict):
        for key, value in v_dict.items():
            selector = f'[name = {key}]'
            self.driver.find_element(By.CSS_SELECTOR, selector).send_key(value)
            self.driver.clear()


    def click_submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.values)
        )
        return self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()




