import allure

from stellar_burgers.api_client import StellarApiClient
from tests.helpers import auth_header, get_ingredient_ids


@allure.feature("Orders")
@allure.story("Create order")
class TestCreateOrder:
    def test_create_order_with_authorization_and_ingredients_success(self, api: StellarApiClient, registered_user):
        token = registered_user["access_token"]
        ingredient_ids = get_ingredient_ids(api, limit=2)

        resp = api.post("/orders", json={"ingredients": ingredient_ids}, headers=auth_header(token))

        assert resp.status_code == 200
        assert resp.json.get("success") is True
        assert resp.json.get("order", {}).get("number") is not None

    def test_create_order_without_authorization_and_ingredients_success(self, api: StellarApiClient):
        ingredient_ids = get_ingredient_ids(api, limit=2)

        resp = api.post("/orders", json={"ingredients": ingredient_ids})

        assert resp.status_code == 200
        assert resp.json.get("success") is True
        assert resp.json.get("order", {}).get("number") is not None

    def test_create_order_without_ingredients_returns_400(self, api: StellarApiClient):
        resp = api.post("/orders", json={"ingredients": []})

        assert resp.status_code == 400
        assert resp.json.get("success") is False
        assert resp.json.get("message") == "Ingredient ids must be provided"

    def test_create_order_with_invalid_ingredient_hash_returns_400(self, api: StellarApiClient):
        # Current API version validates ingredient ids and returns 400 for incorrect values.
        resp = api.post("/orders", json={"ingredients": ["invalid_hash"]})

        assert resp.status_code == 400
        assert resp.json.get("success") is False
        assert "incorrect" in (resp.json.get("message") or "").lower()


@allure.feature("Orders")
@allure.story("Get user orders")
class TestGetUserOrders:
    def test_get_orders_authorized_user_success(self, api: StellarApiClient, registered_user):
        token = registered_user["access_token"]

        resp = api.get("/orders", headers=auth_header(token))

        assert resp.status_code == 200
        assert resp.json.get("success") is True
        assert "orders" in resp.json

    def test_get_orders_unauthorized_user_returns_401(self, api: StellarApiClient):
        resp = api.get("/orders")

        assert resp.status_code == 401
        assert resp.json.get("success") is False
        assert resp.json.get("message") == "You should be authorised"
