import pytest
import allure
import requests
import random

@allure.feature("Проверка API")
@allure.title("Проверка списка пользователей")
def test_list_users(api_client):
    with allure.step("Подготовка данных"):
        headers, base_url = api_client
        url = f"{base_url}/users"
    with allure.step("Отправка запроса"):    
        response = requests.get(url, headers=headers)
    with allure.step("Проверка ответа"):  
        assert response.ok
        result = response.json()
        assert len(result) > 0

@allure.title("Проверка обновление данных о пользователе")
def test_update_user(api_client, create_new_user):
    with allure.step("Подготовка данных"):
        test_number = random.randint(0, 999)
        headers, base_url = api_client
        url = f"{base_url}/users/{create_new_user}"
        new_user = {
            "name":"Nezhen",
            "gender":"male",
            "email":f"testemail{test_number}@gmail.com",
            "status":"active"
        }
    with allure.step("Отправка запроса"):
        response = requests.patch(url, json=new_user, headers=headers)
    with allure.step("Проверка ответа"): 
        assert response.ok
        result = response.json()
        assert len(result) > 0

