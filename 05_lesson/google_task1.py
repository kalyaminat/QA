from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManage
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



driver.get("https://www.google.com/")
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(5)
search_input = "button"

search_input = driver.find_element(By.CSS_SELECTOR, search_input)
for i in range(5):
    search_input.send_keys(Keys.RETURN)
sleep(2)
search_input2 = ".added-manually"
button = driver.find_elements(By.CSS_SELECTOR, search_input2)
print(len(button))

driver.quit()