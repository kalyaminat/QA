from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/inputs')

input = driver.find_element(By.CSS_SELECTOR, '[type="number"]')

input.send_keys('1000')
sleep(2)
input.clear()

input.send_keys('999')

sleep(5)

driver.quit()