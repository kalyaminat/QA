from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
driver.get("http://uitestingplayground.com/dynamicid")
sleep(5)
search_input = '.btn-primary'
search_input = driver.find_element(By.CSS_SELECTOR, search_input)
search_input.send_keys(Keys.RETURN)
sleep(5)

driver.quit()