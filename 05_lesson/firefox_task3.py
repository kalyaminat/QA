from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
search_field = "input#username"
input = driver.find_element(By.CSS_SELECTOR, search_field)
input.send_keys('tomsmith')
search_field1 = "input#password"
input1 = driver.find_element(By.CSS_SELECTOR, search_field1)
input1.send_keys('SuperSecretPassword!')
sleep(2)
search_field2 = "button.radius"
input2 = driver.find_element(By.CSS_SELECTOR, search_field2)
input2.send_keys(Keys.RETURN)
sleep(5)
driver.quit()