from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.support import expected_conditions as EC

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
#driver.find_element(By.LINK_TEXT, '[src="img/award.png"]')


img = WebDriverWait(driver, 40, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img#landscape')))
#ждем появления последней картинки


images = driver.find_elements(By.CSS_SELECTOR, 'img')
image = images[2].get_attribute('src')
print(image)



