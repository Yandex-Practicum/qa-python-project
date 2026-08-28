import allure
import pytest

from constants import INVALID_CREDENTIALS_MESSAGE
from data import generate_user_data


@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.title("Существующий пользователь может войти")
    def test_login_existing_user_success(self, api_client, registered_user):
        payload = registered_user["payload"]

        response = api_client.login_user(
            {"email": payload["email"], "password": payload["password"]}
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["user"]["email"] == payload["email"]
        assert response_body["user"]["name"] == payload["name"]
        assert response_body["accessToken"].startswith("Bearer ")
        assert response_body["refreshToken"]

    @allure.title("Нельзя войти с неверным значением поля: {invalid_field}")
    @pytest.mark.parametrize(
        "invalid_field",
        ["email", "password"],
        ids=["invalid_email", "invalid_password"],
    )
    def test_login_with_invalid_credentials_returns_error(
        self, api_client, registered_user, invalid_field
    ):
        payload = registered_user["payload"]
        credentials = {
            "email": payload["email"],
            "password": payload["password"],
        }
        credentials[invalid_field] = generate_user_data()[invalid_field]

        response = api_client.login_user(credentials)

        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": INVALID_CREDENTIALS_MESSAGE,
        }

