import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_01_form(driver):


    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(30)


    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.clear()
    first_name.send_keys('Иван')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.clear()
    last_name.send_keys('Петров')


    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.clear()
    address.send_keys('Ленина, 55-3')


    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.clear()
    email.send_keys('test@skypro.com')


    phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone_number.clear()
    phone_number.send_keys('+7985899998787')


    zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zip_code.clear()
    zip_code.send_keys('')


    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.clear()
    city.send_keys('Москва')


    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.clear()
    country.send_keys('Россия')


    job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
    job_position.clear()
    job_position.send_keys('QA')


    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.clear()
    company.send_keys('SkyPro')


    #WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, "#company"))
# пока все данные не загрузятся
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()




    assert "success" in driver.find_element(By.ID, "first-name").get_attribute("class")

    assert "success" in driver.find_element(By.ID, "last-name").get_attribute("class")

    assert "success" in driver.find_element(By.ID, "address").get_attribute("class")

    assert "success" in driver.find_element(By.ID, "e-mail").get_attribute("class")

    assert "success" in driver.find_element(By.ID, "phone").get_attribute("class")

    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

    assert "success" in driver.find_element(By.ID, "city").get_attribute("class")

    assert "success" in driver.find_element(By.ID, "country").get_attribute("class")

    assert "success" in driver.find_element(By.ID, "job-position").get_attribute("class")



























