import allure

from utils.helpers import create_order


@allure.suite("Заказы")
class TestOrders:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_token, ingredient_ids):
        headers = {
            "Authorization": auth_token
        }
        payload = {
            "ingredients": ingredient_ids
        }

        response = create_order(payload=payload, headers=headers)
        body = response.json()

        assert response.status_code == 200
        assert "order" in body
        assert body["order"]["number"] > 0
        assert body["order"]["ingredients"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, ingredient_ids):
        payload = {
            "ingredients": ingredient_ids
        }

        response = create_order(payload=payload)
        body = response.json()

        assert response.status_code == 200
        assert "order" in body
        assert body["order"]["number"] > 0

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        payload = {}

        response = create_order(payload=payload)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с некорректным id ингредиента")
    def test_create_order_with_invalid_ingredient_id(self):
        payload = {
            "ingredients": ["invalid_hash"]
        }

        response = create_order(payload=payload)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "One or more ids provided are incorrect"
