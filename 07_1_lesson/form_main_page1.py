from selenium.webdriver.common.by import By


class mainPageForm:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Найти и заполнить поля формы
    def find_element(self, element, value):
        self.driver.find_element(By.NAME, element).send_keys(value)

# Нажат кнопку подтвердить
    def submit(self):
        self.driver.find_element(By.XPATH, '//button[text() = "Submit"]').click()

# Проверить соответсвие цвета полей ожидаемому результату
    def check(self, element):
        return self.driver.find_element(By.ID, element).get_attribute("class")