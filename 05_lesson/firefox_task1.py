
from time import sleep
#driver = webdriver.Firefox()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/entry_ad")
#input = driver.send_keys(Keys.RETURN)
sleep(5)
search_field = ".modal-footer"

search_input = driver.find_element(By.CSS_SELECTOR, search_field).click()

#search_input.send_keys(Keys.RETURN)
sleep(5)

driver.quit()