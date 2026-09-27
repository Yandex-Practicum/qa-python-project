import allure
import pytest
from helpers.api import register_user, register_user_incomplete


class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, created_user, unique_user_data):
        assert created_user["email"] == unique_user_data["email"]
        assert created_user["name"] == unique_user_data["name"]
        assert created_user["access_token"].startswith("Bearer ")
        assert created_user["refresh_token"]

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_already_registered_user(self, created_user):
        response = register_user(
            created_user["email"],
            created_user["password"],
            created_user["name"]
        )
        assert response.status_code == 403
        body = response.json()
        assert body["success"] is False
        assert body["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, unique_user_data, missing_field):
        payload = unique_user_data.copy()
        del payload[missing_field]
        response = register_user_incomplete(payload)
        assert response.status_code == 403
        body = response.json()
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"