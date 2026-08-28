import allure
import pytest

from constants import REQUIRED_FIELDS_MESSAGE, USER_ALREADY_EXISTS_MESSAGE
from data import generate_user_data


@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Можно создать уникального пользователя")
    def test_create_unique_user_success(self, user_factory):
        payload, response = user_factory()
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["user"]["email"] == payload["email"]
        assert response_body["user"]["name"] == payload["name"]
        assert response_body["accessToken"].startswith("Bearer ")
        assert response_body["refreshToken"]

    @allure.title("Нельзя повторно зарегистрировать существующего пользователя")
    def test_create_duplicate_user_returns_error(self, user_factory):
        payload, first_response = user_factory()
        assert first_response.status_code == 200

        second_response = user_factory(payload)[1]

        assert second_response.status_code == 403
        assert second_response.json() == {
            "success": False,
            "message": USER_ALREADY_EXISTS_MESSAGE,
        }

    @allure.title("Нельзя создать пользователя без обязательного поля: {missing_field}")
    @pytest.mark.parametrize(
        "missing_field",
        ["email", "password", "name"],
        ids=["without_email", "without_password", "without_name"],
    )
    def test_create_user_without_required_field_returns_error(
        self, api_client, missing_field
    ):
        payload = generate_user_data()
        payload.pop(missing_field)

        response = api_client.create_user(payload)

        assert response.status_code == 403
        assert response.json() == {
            "success": False,
            "message": REQUIRED_FIELDS_MESSAGE,
        }

