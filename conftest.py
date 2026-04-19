import pytest
from helpers import generate_user, create_user, delete_user


@pytest.fixture
def new_user():
    user = generate_user()
    response = create_user(user)
    
    assert response.status_code == 200
    assert "accessToken" in response.json()
    
    token = response.json()["accessToken"]

    yield user, token

    delete_user(token)