import pytest
from utils.helpers import register_user, login_user, get_ingredients


@pytest.fixture
def registered_user():
    user_data, response = register_user()
    return user_data

@pytest.fixture
def auth_token():
    user_data, _ = register_user()
    response = login_user(
        user_data["email"],
        user_data["password"]
    )
    return response.json()["accessToken"]


@pytest.fixture
def ingredient_ids():
    ingredients = get_ingredients()
    return [ingredients[0]["_id"], ingredients[1]["_id"]]