import allure

from stellar_burgers.api_client import StellarApiClient


@allure.feature("User")
@allure.story("Login")
class TestUserLogin:
    def test_login_existing_user_success(self, api: StellarApiClient, registered_user):
        payload = registered_user["payload"]
        resp = api.post("/auth/login", json={"email": payload["email"], "password": payload["password"]})

        assert resp.status_code == 200
        assert resp.json.get("success") is True
        assert "accessToken" in resp.json
        assert "refreshToken" in resp.json
        assert resp.json.get("user", {}).get("email") == payload["email"]

    def test_login_with_wrong_credentials_returns_401(self, api: StellarApiClient, registered_user):
        payload = registered_user["payload"]
        resp = api.post("/auth/login", json={"email": payload["email"], "password": "wrong_password"})

        assert resp.status_code == 401
        assert resp.json.get("success") is False
        assert resp.json.get("message") == "email or password are incorrect"
