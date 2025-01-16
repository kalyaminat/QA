import requests
import json
from settings import LOGIN, PASSWORD, COMPANY_ID, KEY, BASIC_URL


class Yougile:
    def __init__(self):
        self.login = LOGIN
        self.password = PASSWORD
        self.company_id = COMPANY_ID
        self.url = BASIC_URL

    def get_auth_key(self):
        payload = {
            "login": LOGIN,
            "password": self.password,
            "companyId": self.company_id
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(f'{self.url}' + 'auth/keys', json=payload, headers=headers)
        response.raise_for_status()
        return response.json()


    def create_project(self, url,payload, headers):
        self.url = BASIC_URL
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.url+'projects', json=payload, headers=headers)
        return response(json)

    def get_list(self, url, headers):
        self.url = BASIC_URL
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(self.url+'projects', headers=headers)
        return response.json()

    def change_by_id(self, url, payload, headers):
        self.url = BASIC_URL
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.url + 'projects/{ID}', json=payload, headers=headers)
        return response.json()


    def get_by_id(self, url, payload, headers):
        self.url = BASIC_URL
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.url + 'projects/{ID}', json=payload, headers=headers)
        return response.json()


    def get_auth_key_wrong_password(self, url, payload, headers):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(self.url + 'auth/keys', json=payload, headers=headers)
        return response.json()

    def get_list_wrong_url(self, headers):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.url + 'projects', headers=headers)
        return response.json()["count"]

    def get_by_wrong_id(self, url, headers):
        self.url = BASIC_URL
        headers = {
                'Content-Type': 'application/json'
            }
        response = requests.get(self.url + 'projects/"4f6f0391-0f94-4d30-9b0e-99430a36d4fb"', headers=headers)
        return response.json()






















