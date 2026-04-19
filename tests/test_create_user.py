import pytest
import allure
import requests
from helpers import generate_user, create_user,delete_user
from data.urls import BASE_URL, REGISTER
from data.expected_data import *
from data.payload_data import REQUIRED_USER_FIELDS


@allure.title("Создание уникального пользователя")
def test_create_unique_user():
    user = generate_user()
    response = create_user(user)
    
    token = response.json()["accessToken"]

    assert response.json()["success"] is True
    delete_user(token)

@allure.title("Создание уже существующего пользователя")
def test_create_existing_user():
    user = generate_user()
    first_response = create_user(user)
    token = first_response.json()["accessToken"]

    response = create_user(user)
    
    assert response.status_code == ExpectedResponceCodes.CREATE_DUPLICATE_USER
    assert response.json()["success"] is False
    assert response.json()["message"] == ExpectedResponces.CREATE_DUPLICATE_USER
    delete_user(token)

@pytest.mark.parametrize("payload", REQUIRED_USER_FIELDS)
@allure.title("Создание пользователя без обязательного поля")
def test_create_user_without_required_field(payload):
    user = generate_user()
    del user[payload]

    response = requests.post(
        BASE_URL + REGISTER,
        json=user
    )
    assert response.status_code == ExpectedResponceCodes.CREATE_USER_WITHOUT_ANY_PARAM
    assert response.json()["success"] is False
    assert response.json()["message"] == ExpectedResponces.CREATE_USER_WITHOUT_ANY_PARAM
    