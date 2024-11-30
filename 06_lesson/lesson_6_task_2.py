from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")
input = driver.find_element(By.CSS_SELECTOR, '.form-control')
input.send_keys('SkyPro')
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text



print(button)
