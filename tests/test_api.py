import pytest
import allure
import requests
import random

def test_list_users(api_client):
    headers, base_url = api_client
    url = f"{base_url}/users"
    response = requests.get(url, headers=headers)
    assert response.ok
    result = response.json()
    assert len(result) > 0

def test_update_user(api_client, test_create_new_user):
    test_number = random.randint(0, 999)
    headers, base_url = api_client
    url = f"{base_url}/users/{test_create_new_user}"
    new_user = {
        "name":"Nezhen",
        "gender":"male",
        "email":f"testemail{test_number}@gmail.com",
        "status":"active"
    }
    response = requests.patch(url, json=new_user, headers=headers)
    assert response.ok
    result = response.json()
    print(result)
    assert len(result) > 0

