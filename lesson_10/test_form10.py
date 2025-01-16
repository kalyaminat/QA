from selenium.webdriver.chrome.webdriver import WebDriver
from form_main_page10 import mainPageForm
import pytest
from selenium import webdriver
import allure

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

@allure.title("Заполнение полей формы")
@allure.description("Заполнение полей формы, отправка данных, проверка цвета полей")
@allure.severity("critical")
def test_form(browser: WebDriver):

    with allure.step("Создание экземпляра класса"):
        mainpage = mainPageForm(browser)
    with allure.step("Заполнение поля first-name"):
        mainpage.find_element("first-name", "Иван")
    with allure.step("Заполнение поля last-name"):
        mainpage.find_element("last-name", "Петров")
    with allure.step("Заполнение поля address"):
        mainpage.find_element("address", "Ленина, 55-3")
    with allure.step("Заполнение поля e-mail"):
        mainpage.find_element("e-mail", "test@skypro.com")
    with allure.step("Заполнение поля phone"):
        mainpage.find_element("phone", "+7985899998787")
    with allure.step("Заполнение поля city"):
        mainpage.find_element("city", "Москва")
    with allure.step("Заполнение поля country"):
        mainpage.find_element("country", "Россия")
    with allure.step("Заполнение поля job-position"):
        mainpage.find_element("job-position", "QA")
    with allure.step("Заполнение поля company"):
        mainpage.find_element("company", "SkyPro")

    with allure.step("Отправка данных"):
        mainpage.submit()

    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("first-name")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("last-name")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("address")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("e-mail")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("phone")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("city")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("country")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("job-position")
    with allure.step("Проверка зеленого цвета поля"):
        assert "success" in mainpage.check("company")
    with allure.step("Проверка красного цвета поля"):
        assert "danger" in mainpage.check("zip-code")