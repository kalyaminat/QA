import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = driver.find_element(By.CSS_SELECTOR, 'input#delay')
    delay.clear()
    delay.send_keys('45')

    operations = ['7', '+', '8', '=']
    for op in operations:
        driver.find_element(By.XPATH, f"//span[text()='{op}']").click()


    WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))


    result = driver.find_element(By.CSS_SELECTOR, '.screen').text
    expected = '15'

    assert result == expected

