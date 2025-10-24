import pytest
import requests
import allure
from tests import urls
from tests.data_generator import DataGenerator
from utils.allure_attach import attach_request_response


@allure.feature("API Тесты для заказов")
@allure.story("Создание заказа")
class TestOrderCreation:

    @allure.title("TC-06: Создание заказа с авторизацией и ингредиентами")
    @allure.description("Тест проверяет создание заказа авторизованным пользователем с валидными ингредиентами")
    def test_create_order_with_auth_and_ingredients_success(self, registered_user, ingredient_data, api_available):
        with allure.step("Подготовить данные заказа"):
            valid_ingredients = [ingredient_data[0]["_id"], ingredient_data[1]["_id"]]
            order_data = {"ingredients": valid_ingredients}
            headers = {"Authorization": registered_user["token"]}

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(f"{urls.BASE_URL}/orders", json=order_data, headers=headers)
            attach_request_response(response)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is True, "Поле success должно быть True"
            assert "order" in response_data, "В ответе должно быть поле order"
            assert "number" in response_data["order"], "В заказе должен быть номер"
            assert "name" in response_data["order"], "В заказе должно быть название"

    @allure.title("TC-07: Создание заказа без авторизации")
    @allure.description("Тест проверяет создание заказа без авторизации")
    def test_create_order_without_auth_success(self, ingredient_data, api_available):
        with allure.step("Подготовить данные заказа"):
            valid_ingredients = [ingredient_data[0]["_id"], ingredient_data[1]["_id"]]
            order_data = {"ingredients": valid_ingredients}

        with allure.step("Отправить запрос на создание заказа без авторизации"):
            response = requests.post(f"{urls.BASE_URL}/orders", json=order_data)
            attach_request_response(response)

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is True, "Поле success должно быть True"
            assert "order" in response_data, "В ответе должно быть поле order"

    @allure.title("TC-08: Создание заказа без ингредиентов")
    @allure.description("Тест проверяет попытку создания заказа без указания ингредиентов")
    def test_create_order_without_ingredients_fail(self, registered_user, api_available):
        with allure.step("Подготовить данные заказа без ингредиентов"):
            order_data = {"ingredients": []}
            headers = {"Authorization": registered_user["token"]}

        with allure.step("Отправить запрос без ингредиентов"):
            response = requests.post(f"{urls.BASE_URL}/orders", json=order_data, headers=headers)
            attach_request_response(response)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is False, "Поле success должно быть False"
            assert "ingredients" in response_data["message"].lower(), "Сообщение должно содержать информацию об ингредиентах"

    @allure.title("TC-09: Создание заказа с неверным хешем ингредиентов")
    @allure.description("Тест проверяет попытку создания заказа с невалидными хешами ингредиентов")
    def test_create_order_with_invalid_ingredient_hash_fail(self, registered_user, api_available):
        with allure.step("Подготовить невалидные хеши ингредиентов"):
            generator = DataGenerator()
            invalid_hashes = [generator.generate_random_hash() for _ in range(2)]
            order_data = {"ingredients": invalid_hashes}
            headers = {"Authorization": registered_user["token"]}

        with allure.step("Отправить запрос с невалидными хешами"):
            response = requests.post(f"{urls.BASE_URL}/orders", json=order_data, headers=headers)
            attach_request_response(response)

        with allure.step("Проверить ошибку обработки ингредиентов"):
            # Согласно документации API должен возвращать 400 при невалидных ингредиентах
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is False, "Поле success должно быть False"

    @allure.title("TC-10: Создание заказа с одним ингредиентом")
    @allure.description("Тест проверяет создание заказа с минимальным количеством ингредиентов")
    def test_create_order_with_single_ingredient_success(self, registered_user, ingredient_data, api_available):
        with allure.step("Подготовить данные заказа с одним ингредиентом"):
            single_ingredient = [ingredient_data[0]["_id"]]
            order_data = {"ingredients": single_ingredient}
            headers = {"Authorization": registered_user["token"]}

        with allure.step("Отправить запрос с одним ингредиентом"):
            response = requests.post(f"{urls.BASE_URL}/orders", json=order_data, headers=headers)
            attach_request_response(response)

        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
            response_data = response.json()
            assert response_data["success"] is True, "Поле success должно быть True"
