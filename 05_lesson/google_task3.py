from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("https://www.google.com/")
driver.get("http://uitestingplayground.com/classattr")
sleep(5)
search_field = 'button.btn-primary.btn-test'
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys(Keys.RETURN)
sleep(5)

driver.quit()