import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from form_main_page import FormMainPage
from filled_form import FilledForm

v_dict = {'first-name': 'Иван', 'last-name': 'Петров', 'address': 'Ленина, 55-3', 'e-mail': 'test@skypro.com', 'city': 'Москва',
               'country': 'Россия', 'job-position': 'QA', 'phone': '+7985899998787', 'company': 'SkyPro', 'zip-code': ''
          }

id_values = ["first-name","last-name", "address", "phone", "zip-code", "city", "country", "e-mail", "phone",
             "job-position", "company"]

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()

def TestForm(driver):
    main_page = FormMainPage(driver)
    main_page.fill_cell()
    main_page.click_submit()

    filled_form = FilledForm(driver)
    filled_form.find_fields(id_values)
    # filled_form.get_class('first-name')
    # filled_form.get_class('last-name')
    # filled_form.get_class('address')
    # filled_form.get_class('zip-code')
    # filled_form.get_class('city')
    # filled_form.get_class('country')
    # filled_form.get_class('email')
    # filled_form.get_class('phone')
    # filled_form.get_class('job-position')
    # filled_form.get_class('company')

    assert 'success' in filled_form.get_class('first-name')
    assert 'success' in filled_form.get_class('last-name')
    assert 'success' in filled_form.get_class('address')
    assert 'danger' in filled_form.get_class("zip-code")
    assert 'success' in filled_form.get_class('city')
    assert 'success' in filled_form.get_class('country')
    assert 'success' in filled_form.get_class('email')
    assert 'success' in filled_form.get_class('phone')
    assert 'success' in filled_form.get_class('job-position')
    assert 'success' in filled_form.get_class('company')









