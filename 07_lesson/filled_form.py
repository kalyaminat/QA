from form_main_page import FormMainPage
from selenium.webdriver.common.by import By

id_values = list()

class FilledForm:
    def __init__(self, driver):
        self.driver = driver

    def  find_fields(self, ID: [id_values]):
        for id_value in id_values:
            self.driver.find_element(By.ID, id_value)

    def get_class(self, driver):
        self.driver.find_element().get_attribute('class')





