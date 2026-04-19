import pytest
import allure
import requests
from data.urls import BASE_URL, ORDERS
from data.payload_data import VALID_INGREDIENTS, INVALID_INGREDIENT
from data.expected_data import *

@pytest.mark.parametrize("case_name,ingredients",VALID_INGREDIENTS)
def test_create_order_authorized(new_user,case_name,ingredients):
    allure.dynamic.title(f"Создание заказа с авторизацией: {case_name}")
    _, token = new_user
    response = requests.post(
        BASE_URL + ORDERS,
        headers={"Authorization": token},
        json={"ingredients":ingredients}
    )

    assert response.status_code == 200
    assert response.json()["success"] is True

@pytest.mark.parametrize("case_name,ingredients",VALID_INGREDIENTS)
def test_create_order_without_auth(case_name,ingredients):
    allure.dynamic.title(f"Создание заказа без авторизации: {case_name} ")
    response = requests.post(
        BASE_URL + ORDERS,
        json={"ingredients": ingredients}
    )

    assert response.status_code == ExpectedResponceCodes.CREATE_ORDER_UNAUTORIZED_USER


@allure.title("Создание заказа без ингредиентов")
def test_create_order_without_ingredients():
    response = requests.post(
        BASE_URL + ORDERS,
        json={"ingredients": []}
    )

    assert response.status_code == ExpectedResponceCodes.CREATE_ORDER_EMPTY_INGREDIENTS
    assert response.json()["success"] is False
    assert response.json()["message"] == ExpectedResponces.CREATE_ORDER_EMPTY_INGREDIENTS


@allure.title("Создание заказа с неверным хешем ингредиентов")
def test_create_order_invalid_hash():
    response = requests.post(
        BASE_URL + ORDERS,
        json={"ingredients": [INVALID_INGREDIENT]}
    )

    assert response.status_code == ExpectedResponceCodes.CREATE_ORDER_INVALID_INGREDIENT_HASH