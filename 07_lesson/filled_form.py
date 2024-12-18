from form_main_page import FormMainPage
from selenium.webdriver.common.by import By

id_values = list()

class FilledForm:
    def __init__(self, driver):
        self.driver = driver

    def  find_fields(self, id_values):
        for id_value in id_values:
            self.driver.find_element(By.ID, id_value)

    def get_class(self, id_value):
        return self.driver.find_element(By.ID, id_value).get_attribute('class')
        #self.driver.find_element().get_attribute('class')






