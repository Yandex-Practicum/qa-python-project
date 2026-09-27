import allure
from helpers.api import login_user


class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, created_user):
        response = login_user(created_user["email"], created_user["password"])

        assert response.status_code == 200
        body = response.json()

        assert body["success"] is True
        assert "accessToken" in body
        assert body["accessToken"].startswith("Bearer ")
        assert "refreshToken" in body
        assert body["user"]["email"] == created_user["email"]
        assert body["user"]["name"] == created_user["name"]

    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_wrong_credentials(self, created_user):
        response = login_user(created_user["email"], "WrongPassword123!")

        assert response.status_code == 401
        body = response.json()

        assert body["success"] is False
        assert body["message"] == "email or password are incorrect"