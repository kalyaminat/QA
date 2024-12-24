from yougile import Yougile
from settings import LOGIN, PASSWORD, COMPANY_ID, KEY, BASIC_URL, USER_ID
import requests
import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_yougile():
    yougile = Yougile()
    yougile.get_auth_key()
    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = yougile.get_auth_key()
    return response ["key"]
    assert len(response["key"]) == 64

    yougile.create_project(BASIC_URL, payload, headers)
    payload = {
  "title": "ГосУслуги",
  "users": {
    USER_ID: "admin"
  }
}
    ID = yougile.create_project()['id']
    assert len(ID) == 1

    yougile.get_list()
    response = yougile.get_list
    assert response["content"]["title"][1] == "Госуслуги"
    assert len(response["content"]) >= 0

    yougile.change_by_id()
    payload = {
        "deleted": True,
        "title": "Гос-Услуги",
        "users": {
            USER_ID: "admin"

        }
    }
    response = yougile.change_by_id()
    assert response["id"] == ID


    yougile.get_by_id()
    payload = {ID}
    response = yougile.get_by_id()
    assert response["users"] == "admin"
    assert response["title"] == "Гос-Услуги"


    yougile.get_auth_key_wrong_password()
    payload = {
        "login": LOGIN,
        "password": "123456789",
        "companyId": COMPANY_ID
    }
    response = yougile.get_auth_key_wrong_password()
    assert response["statusCode"] in [401, 400]

    yougile.get_list_wrong_url()
    url = "https://ru.yougile.com/api-v2}}}!!!"
    response = yougile.get_list_wrong_url()
    assert response["statusCode"] == 404

    yougile.get_by_wrong_id()
    response =  yougile.get_by_wrong_id()
    assert response["statusCode"] == 404














