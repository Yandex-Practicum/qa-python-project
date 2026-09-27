import allure
from helpers.api import create_order


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, created_user, ingredients):
        ingredient_ids = [ingredients[0]["_id"], ingredients[1]["_id"], ingredients[2]["_id"]]

        response = create_order(ingredient_ids, created_user["access_token"])

        assert response.status_code == 200
        body = response.json()

        assert body["success"] is True
        assert "name" in body
        assert "order" in body
        assert "number" in body["order"]
        assert body["order"]["number"] > 0

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, ingredients):
        ingredient_ids = [ingredients[0]["_id"], ingredients[1]["_id"]]

        response = create_order(ingredient_ids)

        assert response.status_code == 200
        body = response.json()

        assert body["success"] is True
        assert "name" in body
        assert "order" in body
        assert "number" in body["order"]

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, ingredients):
        ingredient_ids = [
            ingredients[0]["_id"],
            ingredients[3]["_id"],
            ingredients[5]["_id"]
        ]

        response = create_order(ingredient_ids)

        assert response.status_code == 200
        body = response.json()
        assert body["success"] is True
        assert body["order"]["number"] > 0

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = create_order([])

        assert response.status_code == 400
        body = response.json()

        assert body["success"] is False
        assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_hash(self):
        response = create_order(["60d3463f7034a000269f45e9INVALID"])

        assert response.status_code == 500