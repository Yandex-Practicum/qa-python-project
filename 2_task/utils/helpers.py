import random
import string
import requests
import allure

from utils.urls import BASE_URL


def random_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@mail.ru"


def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def random_name():
    return ''.join(random.choices(string.ascii_letters, k=6))


@allure.step("Регистрация пользователя")
def register_user(payload=None):
    if payload is None:
        payload = {
            "email": random_email(),
            "password": random_password(),
            "name": random_name()
        }

    response = requests.post(
        f"{BASE_URL}/api/auth/register",
        json=payload
    )
    return payload, response


@allure.step("Логин пользователя")
def login_user(email, password):
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json=payload
    )
    return response


@allure.step("Получение списка ингредиентов")
def get_ingredients():
    response = requests.get(
        f"{BASE_URL}/api/ingredients"
    )
    return response.json()["data"]


@allure.step("Создание заказа")
def create_order(payload, headers=None):
    response = requests.post(
        f"{BASE_URL}/api/orders",
        json=payload,
        headers=headers
    )
    return response
