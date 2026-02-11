import allure
import pytest

from utils.helpers import login_user


@allure.suite("Логин пользователя")
class TestUserLogin:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, registered_user):
        response = login_user(
            email=registered_user["email"],
            password=registered_user["password"]
        )

        body = response.json()

        assert response.status_code == 200
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == registered_user["email"]

    @allure.title("Логин с неверным логином и паролем")
    def test_login_with_invalid_credentials(self):
        response = login_user(
            email="wrong@mail.ru",
            password="wrongpassword"
        )

        body = response.json()

        assert response.status_code in [401, 403]
        assert body["message"] == "email or password are incorrect"

    @allure.title("Логин без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password"])
    def test_login_without_required_field(self, missing_field):
        payload = {
            "email": "test@mail.ru",
            "password": "password123"
        }
        payload.pop(missing_field)

        # вызываем helper напрямую с некорректными данными
        response = login_user(
            email=payload.get("email"),
            password=payload.get("password")
        )

        body = response.json()

        assert response.status_code in [401, 403]
        assert body["message"] == "email or password are incorrect"
