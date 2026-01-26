import pytest

@pytest.fixture()
def api_client():
    token = "8a9e0b0229586c423143abefaa395d29f03db9a20fb5ccd70262a45053b54467"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    base_url = "https://gorest.co.in/public/v2"

    return headers, base_url
