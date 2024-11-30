from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20) #поместим метод перед переходом на сайт
driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()