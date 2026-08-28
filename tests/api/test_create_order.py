import allure

from constants import INGREDIENTS_REQUIRED_MESSAGE, UNAUTHORIZED_MESSAGE


@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Авторизованный пользователь может создать заказ")
    def test_create_order_with_authorization_success(
        self, api_client, registered_user, ingredient_ids
    ):
        response = api_client.create_order(
            ingredient_ids[:1], registered_user["access_token"]
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert isinstance(response_body["order"]["number"], int)

    @allure.title("Неавторизованный пользователь не может создать заказ")
    def test_create_order_without_authorization_returns_error(
        self, api_client, ingredient_ids
    ):
        response = api_client.create_order(ingredient_ids)

        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": UNAUTHORIZED_MESSAGE,
        }

    @allure.title("Можно создать заказ с несколькими ингредиентами")
    def test_create_order_with_ingredients_success(
        self, api_client, registered_user, ingredient_ids
    ):
        response = api_client.create_order(
            ingredient_ids, registered_user["access_token"]
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["name"]
        assert isinstance(response_body["order"]["number"], int)

    @allure.title("Нельзя создать заказ без ингредиентов")
    def test_create_order_without_ingredients_returns_error(
        self, api_client, registered_user
    ):
        response = api_client.create_order([], registered_user["access_token"])

        assert response.status_code == 400
        assert response.json() == {
            "success": False,
            "message": INGREDIENTS_REQUIRED_MESSAGE,
        }

    @allure.title("Нельзя создать заказ с неверным хешем ингредиента")
    def test_create_order_with_invalid_ingredient_hash_returns_error(
        self, api_client, registered_user
    ):
        response = api_client.create_order(
            ["invalid-ingredient-hash"], registered_user["access_token"]
        )

        assert response.status_code == 500
