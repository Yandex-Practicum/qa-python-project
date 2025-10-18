import pytest
import requests
import allure
from utils.allure_attach import attach_request_response


@allure.feature("API Тесты для заказов")
@allure.story("Создание заказа")
class TestOrderCreation:

    @allure.title("TC-06: Создание заказа с авторизацией и ингредиентами")
    @allure.description("Тест проверяет создание заказа авторизованным пользователем с валидными ингредиентами")
    def test_create_order_with_auth_and_ingredients_success(self, base_url, registered_user, auth_header, ingredient_data):
        with allure.step("Подготовить данные заказа"):
            valid_ingredients = [ingredient_data[0]["_id"], ingredient_data[1]["_id"]]
            order_data = {"ingredients": valid_ingredients}

        with allure.step("Отправить запрос на создание заказа с авторизацией"):
            response = requests.post(f"{base_url}/orders", json=order_data, headers=auth_header)
            attach_request_response(response)

        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["success"] is True
            assert "order" in response_data
            assert "number" in response_data["order"]
            assert "name" in response_data["order"]
            assert "status" in response_data["order"]

    @allure.title("TC-07: Создание заказа без авторизации")
    @allure.description("Тест проверяет создание заказа без авторизации")
    def test_create_order_without_auth_success(self, base_url, ingredient_data):
        with allure.step("Подготовить данные заказа"):
            valid_ingredients = [ingredient_data[0]["_id"], ingredient_data[1]["_id"]]
            order_data = {"ingredients": valid_ingredients}

        with allure.step("Отправить запрос на создание заказа без авторизации"):
            response = requests.post(f"{base_url}/orders", json=order_data)
            attach_request_response(response)

        with allure.step("Проверить успешное создание заказа без авторизации"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["success"] is True
            assert "order" in response_data
            assert "number" in response_data["order"]

    @allure.title("TC-08: Создание заказа без ингредиентов")
    @allure.description("Тест проверяет попытку создания заказа без указания ингредиентов")
    def test_create_order_without_ingredients_fail(self, base_url, auth_header):
        with allure.step("Подготовить данные заказа без ингредиентов"):
            order_data = {"ingredients": []}

        with allure.step("Отправить запрос без ингредиентов"):
            response = requests.post(f"{base_url}/orders", json=order_data, headers=auth_header)
            attach_request_response(response)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400
            response_data = response.json()
            assert response_data["success"] is False
            assert "ingredients" in response_data["message"].lower()

    @allure.title("TC-09: Создание заказа с неверным хешем ингредиентов")
    @allure.description("Тест проверяет попытку создания заказа с невалидными хешами ингредиентов")
    def test_create_order_with_invalid_ingredient_hash_fail(self, base_url, auth_header, data_generator):
        with allure.step("Подготовить невалидные хеши ингредиентов"):
            invalid_hashes = [data_generator.generate_random_hash() for _ in range(2)]
            order_data = {"ingredients": invalid_hashes}

        with allure.step("Отправить запрос с невалидными хешами"):
            response = requests.post(f"{base_url}/orders", json=order_data, headers=auth_header)
            attach_request_response(response)

        with allure.step("Проверить ошибку обработки ингредиентов"):
            # API может возвращать 500 или 400 при невалидных хешах
            assert response.status_code in [400, 500]
            response_data = response.json()
            assert response_data["success"] is False

    @allure.title("TC-10: Создание заказа с одним ингредиентом")
    @allure.description("Тест проверяет создание заказа с минимальным количеством ингредиентов")
    def test_create_order_with_single_ingredient_success(self, base_url, auth_header, ingredient_data):
        with allure.step("Подготовить данные заказа с одним ингредиентом"):
            single_ingredient = [ingredient_data[0]["_id"]]
            order_data = {"ingredients": single_ingredient}

        with allure.step("Отправить запрос с одним ингредиентом"):
            response = requests.post(f"{base_url}/orders", json=order_data, headers=auth_header)
            attach_request_response(response)

        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["success"] is True
