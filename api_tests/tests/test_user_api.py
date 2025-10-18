import pytest
import requests
import allure
from utils.allure_attach import attach_request_response


@allure.feature("API Тесты для пользователей")
@allure.story("Создание пользователя")
class TestUserRegistration:

    @allure.title("TC-01: Успешное создание уникального пользователя")
    @allure.description("Тест проверяет создание нового пользователя с валидными данными")
    def test_create_unique_user_success(self, base_url, data_generator):
        with allure.step("Подготовить данные нового пользователя"):
            user_data = data_generator.generate_user_data()

        with allure.step("Отправить запрос на создание пользователя"):
            response = requests.post(f"{base_url}/auth/register", json=user_data)
            attach_request_response(response)

        with allure.step("Проверить успешное создание пользователя"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["success"] is True
            assert "accessToken" in response_data
            assert "refreshToken" in response_data
            assert response_data["user"]["email"] == user_data["email"]
            assert response_data["user"]["name"] == user_data["name"]

        with allure.step("Удалить созданного пользователя"):
            token = response_data["accessToken"]
            headers = {"Authorization": token}
            delete_response = requests.delete(f"{base_url}/auth/user", headers=headers)
            assert delete_response.status_code == 202

    @allure.title("TC-02: Создание уже зарегистрированного пользователя")
    @allure.description("Тест проверяет попытку создания пользователя с существующим email")
    def test_create_existing_user_fail(self, base_url, registered_user):
        with allure.step("Попытаться создать пользователя с существующим email"):
            existing_user_data = {
                "email": registered_user["email"],
                "password": "anypassword123",
                "name": "Any Name"
            }
            response = requests.post(f"{base_url}/auth/register", json=existing_user_data)
            attach_request_response(response)

        with allure.step("Проверить ошибку создания пользователя"):
            assert response.status_code == 403
            response_data = response.json()
            assert response_data["success"] is False
            assert response_data["message"] == "User already exists"

    @allure.title("TC-03: Создание пользователя без обязательного поля")
    @allure.description("Тест проверяет создание пользователя без заполнения обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field(self, base_url, data_generator, missing_field):
        with allure.step(f"Подготовить данные пользователя без поля {missing_field}"):
            invalid_user_data = data_generator.generate_user_data()
            invalid_user_data.pop(missing_field)

        with allure.step("Отправить запрос с неполными данными"):
            response = requests.post(f"{base_url}/auth/register", json=invalid_user_data)
            attach_request_response(response)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 403
            response_data = response.json()
            assert response_data["success"] is False
            assert "required field" in response_data["message"].lower()


@allure.feature("API Тесты для пользователей")
@allure.story("Логин пользователя")
class TestUserLogin:

    @allure.title("TC-04: Успешный логин под существующим пользователем")
    @allure.description("Тест проверяет успешную авторизацию с правильными учетными данными")
    def test_login_existing_user_success(self, base_url, registered_user):
        with allure.step("Подготовить данные для логина"):
            login_data = {
                "email": registered_user["email"],
                "password": registered_user["password"]
            }

        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(f"{base_url}/auth/login", json=login_data)
            attach_request_response(response)

        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["success"] is True
            assert "accessToken" in response_data
            assert "refreshToken" in response_data
            assert response_data["user"]["email"] == registered_user["email"]
            assert response_data["user"]["name"] == registered_user["name"]

    @allure.title("TC-05: Логин с неверными учетными данными")
    @allure.description("Тест проверяет попытку авторизации с неверным email и паролем")
    def test_login_with_invalid_credentials_fail(self, base_url, data_generator):
        with allure.step("Подготовить неверные учетные данные"):
            invalid_login_data = data_generator.generate_user_data()

        with allure.step("Отправить запрос с неверными данными"):
            response = requests.post(f"{base_url}/auth/login", json=invalid_login_data)
            attach_request_response(response)

        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 401
            response_data = response.json()
            assert response_data["success"] is False
            assert "email or password are incorrect" in response_data["message"].lower()
