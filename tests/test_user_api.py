import pytest
import requests
import allure
from tests import urls
from tests.data_generator import DataGenerator
from utils.allure_attach import attach_request_response


@pytest.mark.api
@allure.feature("API Тесты для пользователей")
class TestUserRegistration:

    @allure.title("TC-01: Успешное создание уникального пользователя")
    @allure.description("Тест проверяет создание нового пользователя с валидными данными")
    def test_create_unique_user_success(self, temporary_user, api_available):
        # Пользователь уже создан в фикстуре temporary_user, проверяем его данные
        with allure.step("Проверить данные созданного пользователя"):
            # Получаем информацию о пользователе для проверки
            headers = {"Authorization": temporary_user["token"]}
            response = requests.get(f"{urls.BASE_URL}/auth/user", headers=headers)
            attach_request_response(response)

        with allure.step("Проверить успешное создание пользователя"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is True, "Поле success должно быть True"
            assert response_data["user"]["email"] == temporary_user["email"], "Email должен совпадать"
            assert response_data["user"]["name"] == temporary_user["name"], "Имя должно совпадать"
        # Удаление пользователя происходит автоматически в фикстуре temporary_user

    @allure.title("TC-02: Создание уже зарегистрированного пользователя")
    @allure.description("Тест проверяет попытку создания пользователя с существующим email")
    def test_create_existing_user_fail(self, registered_user):
        with allure.step("Попытаться создать пользователя с существующим email"):
            existing_user_data = {
                "email": registered_user["email"],
                "password": "anypassword123",
                "name": "Any Name"
            }
            response = requests.post(f"{urls.BASE_URL}/auth/register", json=existing_user_data)
            attach_request_response(response)

        with allure.step("Проверить ошибку создания пользователя"):
            assert response.status_code == 403, f"Ожидался статус 403, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is False, "Поле success должно быть False"
            assert response_data["message"] == "User already exists", "Сообщение должно указывать на существующего пользователя"

    @allure.title("TC-03: Создание пользователя без обязательного поле")
    @allure.description("Тест проверяет создание пользователя без заполнения обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field(self, api_available, missing_field):
        with allure.step(f"Подготовить данные пользователя без поля {missing_field}"):
            generator = DataGenerator()
            invalid_user_data = generator.generate_user_data()
            invalid_user_data.pop(missing_field)

        with allure.step("Отправить запрос с неполными данными"):
            response = requests.post(f"{urls.BASE_URL}/auth/register", json=invalid_user_data)
            attach_request_response(response)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 403, f"Ожидался статус 403, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is False, "Поле success должно быть False"
            # Проверяем, что в сообщении есть указание на обязательное поле
            assert "field" in response_data["message"].lower(), "Сообщение должно указывать на проблему с полями"


@allure.feature("API Тесты для пользователей")
@allure.story("Логин пользователя")
class TestUserLogin:

    @allure.title("TC-04: Успешный логин под существующим пользователем")
    @allure.description("Тест проверяет успешную авторизацию с правильными учетными данными")
    def test_login_existing_user_success(self, registered_user):
        with allure.step("Подготовить данные для логина"):
            login_data = {
                "email": registered_user["email"],
                "password": registered_user["password"]
            }

        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(f"{urls.BASE_URL}/auth/login", json=login_data)
            attach_request_response(response)

        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is True, "Поле success должно быть True"
            assert "accessToken" in response_data, "В ответе должен быть accessToken"
            assert "refreshToken" in response_data, "В ответе должен быть refreshToken"
            assert response_data["user"]["email"] == registered_user["email"], "Email должен совпадать"
            assert response_data["user"]["name"] == registered_user["name"], "Имя должно совпадать"

    @allure.title("TC-05: Логин с неверными учетными данными")
    @allure.description("Тест проверяет попытку авторизации с неверным email и паролем")
    def test_login_with_invalid_credentials_fail(self, api_available):
        with allure.step("Подготовить неверные учетные данные"):
            generator = DataGenerator()
            invalid_login_data = generator.generate_user_data()

        with allure.step("Отправить запрос с неверными данными"):
            response = requests.post(f"{urls.BASE_URL}/auth/login", json=invalid_login_data)
            attach_request_response(response)

        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is False, "Поле success должно быть False"
            assert "email or password are incorrect" in response_data["message"].lower(), "Сообщение должно указывать на неверные учетные данные"
