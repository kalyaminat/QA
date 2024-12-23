from selenium.webdriver.chrome.webdriver import WebDriver
from form_main_page1 import mainPageForm
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


def test_form(browser: WebDriver):

    mainpage = mainPageForm(browser)
    mainpage.find_element("first-name", "Иван")
    mainpage.find_element("last-name", "Петров")
    mainpage.find_element("address", "Ленина, 55-3")
    mainpage.find_element("e-mail", "test@skypro.com")
    mainpage.find_element("phone", "+7985899998787")
    mainpage.find_element("city", "Москва")
    mainpage.find_element("country", "Россия")
    mainpage.find_element("job-position", "QA")
    mainpage.find_element("company", "SkyPro")

    mainpage.submit()

    assert "success" in mainpage.check("first-name")
    assert "success" in mainpage.check("last-name")
    assert "success" in mainpage.check("address")
    assert "success" in mainpage.check("e-mail")
    assert "success" in mainpage.check("phone")
    assert "success" in mainpage.check("city")
    assert "success" in mainpage.check("country")
    assert "success" in mainpage.check("job-position")
    assert "success" in mainpage.check("company")
    assert "danger" in mainpage.check("zip-code")