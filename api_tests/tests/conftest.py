import pytest
import requests
import allure
from helpers.data_generator import DataGenerator


@pytest.fixture
def base_url():
    return "https://stellarburgers.nomoreparties.site/api"


@pytest.fixture
def data_generator():
    return DataGenerator()


@pytest.fixture
def user_data(data_generator):
    return data_generator.generate_user_data()


@pytest.fixture
def registered_user(base_url, user_data):
    """Фикстура для создания и удаления зарегистрированного пользователя"""
    response = requests.post(f"{base_url}/auth/register", json=user_data)
    assert response.status_code == 200
    token = response.json()["accessToken"]

    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "token": token
    }

    # Удаление пользователя после теста
    headers = {"Authorization": token}
    requests.delete(f"{base_url}/auth/user", headers=headers)


@pytest.fixture
def auth_header(registered_user):
    return {"Authorization": registered_user["token"]}


@pytest.fixture
def ingredient_data(base_url):
    """Фикстура для получения данных об ингредиентах"""
    response = requests.get(f"{base_url}/ingredients")
    assert response.status_code == 200
    ingredients = response.json()["data"]
    return ingredients
