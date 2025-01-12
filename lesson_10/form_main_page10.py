from selenium.webdriver.common.by import By
import allure

class mainPageForm:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Найти и заполнить поля формы")
    def find_element(self, element: str, value: str):
        self.driver.find_element(By.NAME, element).send_keys(value)

    @allure.step("Нажать кнопку подтвердить")
    def submit(self):
        self.driver.find_element(By.XPATH, '//button[text() = "Submit"]').click()

    @allure.step("Проверить соответствие цвета полей ожидаемому результату")
    def check(self, element: str) -> str:
        return self.driver.find_element(By.ID, element).get_attribute("class")