import allure
import requests

from constants import (
    BASE_URL,
    INGREDIENTS_ENDPOINT,
    LOGIN_ENDPOINT,
    ORDERS_ENDPOINT,
    REGISTER_ENDPOINT,
    REQUEST_TIMEOUT,
    USER_ENDPOINT,
)


class StellarBurgersApi:
    def __init__(self):
        self.session = requests.Session()

    def close(self):
        self.session.close()

    @staticmethod
    def _attach_response(response):
        allure.attach(
            f"HTTP {response.status_code}\n{response.text}",
            name="Ответ API",
            attachment_type=allure.attachment_type.TEXT,
        )

    def _request(self, method, endpoint, **kwargs):
        response = self.session.request(
            method,
            f"{BASE_URL}{endpoint}",
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )
        self._attach_response(response)
        return response

    @allure.step("Создать пользователя")
    def create_user(self, payload):
        return self._request("POST", REGISTER_ENDPOINT, json=payload)

    @allure.step("Авторизовать пользователя")
    def login_user(self, payload):
        return self._request("POST", LOGIN_ENDPOINT, json=payload)

    @allure.step("Удалить тестового пользователя")
    def delete_user(self, access_token):
        return self._request(
            "DELETE",
            USER_ENDPOINT,
            headers={"Authorization": access_token},
        )

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        return self._request("GET", INGREDIENTS_ENDPOINT)

    @allure.step("Создать заказ")
    def create_order(self, ingredient_ids, access_token=None):
        headers = {"Authorization": access_token} if access_token else None
        return self._request(
            "POST",
            ORDERS_ENDPOINT,
            json={"ingredients": ingredient_ids},
            headers=headers,
        )

