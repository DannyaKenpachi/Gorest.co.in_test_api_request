import pytest
import random
import requests

@pytest.fixture(scope='session')
def api_client():
    token = "8a9e0b0229586c423143abefaa395d29f03db9a20fb5ccd70262a45053b54467"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    base_url = "https://gorest.co.in/public/v2"

    return headers, base_url

@pytest.fixture(scope='session')
def create_new_user(api_client):
    test_number = random.randint(0, 999)
    headers, base_url = api_client
    url = f"{base_url}/users"
    new_user = {
        "name":"Mezhen",
        "gender":"male",
        "email":f"testemail{test_number}@gmail.com",
        "status":"active"
    }
    response = requests.post(url, json=new_user, headers=headers)
    assert response.ok
    result = response.json()
    assert len(result) > 0
    yield result["id"]
    requests.delete(f"{base_url}/users/{result["id"]}", headers=headers)