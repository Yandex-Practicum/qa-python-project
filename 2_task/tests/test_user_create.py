import allure
import pytest

from utils.helpers import register_user
from data.user_data import get_valid_user


@allure.feature("Создание пользователя")
class TestUserCreate:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        payload = get_valid_user()

        user_data, response = register_user(payload)

        body = response.json()

        assert response.status_code == 200
        assert "accessToken" in body
        assert "refreshToken" in body
        assert "user" in body
        assert body["user"]["email"] == payload["email"]

    @allure.title("Создание уже существующего пользователя")
    def test_create_existing_user(self):
        payload = get_valid_user()

        register_user(payload)
        _, response = register_user(payload)

        body = response.json()

        assert response.status_code == 403
        assert body["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, missing_field):
        payload = get_valid_user()
        payload.pop(missing_field)

        _, response = register_user(payload)
        body = response.json()

        assert response.status_code == 403
        assert body["message"] == "Email, password and name are required fields"
