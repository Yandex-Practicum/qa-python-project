import allure
import requests

BASE_URL = "https://stellarburgers.education-services.ru"


@allure.step("Регистрация пользователя")
def register_user(email: str, password: str, name: str):
    return requests.post(
        f"{BASE_URL}/api/auth/register",
        json={"email": email, "password": password, "name": name}
    )


@allure.step("Удаление пользователя")
def delete_user(access_token: str):
    return requests.delete(
        f"{BASE_URL}/api/auth/user",
        headers={"Authorization": access_token}
    )


@allure.step("Логин пользователя")
def login_user(email: str, password: str):
    return requests.post(
        f"{BASE_URL}/api/auth/login",
        json={"email": email, "password": password}
    )


@allure.step("Создание заказа")
def create_order(ingredient_ids: list, access_token: str = None):
    headers = {}
    if access_token:
        headers["Authorization"] = access_token
    return requests.post(
        f"{BASE_URL}/api/orders",
        json={"ingredients": ingredient_ids},
        headers=headers
    )


@allure.step("Получение списка ингредиентов")
def get_ingredients():
    return requests.get(f"{BASE_URL}/api/ingredients")

@allure.step("Регистрация пользователя с неполными данными")
def register_user_incomplete(payload: dict):
    return requests.post(
        f"{BASE_URL}/api/auth/register",
        json=payload
    )