import pytest
from helpers import generate_user, create_user, delete_user


@pytest.fixture
def new_user():
    user = generate_user()
    response = create_user(user)

    token = response.json()["accessToken"]

    yield user, token

    delete_user(token)