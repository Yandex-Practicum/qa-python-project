import allure
import pytest

from stellar_burgers.api_client import StellarApiClient


@allure.feature("User")
@allure.story("Create user")
class TestUserCreate:
    def test_create_unique_user_success(self, api: StellarApiClient, unique_user_payload):
        resp = api.post("/auth/register", json=unique_user_payload)

        assert resp.status_code == 200
        assert resp.json.get("success") is True
        assert "accessToken" in resp.json
        assert "refreshToken" in resp.json
        assert resp.json.get("user", {}).get("email") == unique_user_payload["email"]

        # cleanup
        access_token = resp.json.get("accessToken")
        if access_token:
            api.delete("/auth/user", headers={"Authorization": access_token})

    def test_create_user_that_already_exists_returns_403(self, api: StellarApiClient, registered_user):
        payload = registered_user["payload"]

        resp = api.post("/auth/register", json=payload)

        assert resp.status_code == 403
        assert resp.json.get("success") is False
        assert resp.json.get("message") == "User already exists"

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field_returns_403(
        self,
        api: StellarApiClient,
        unique_user_payload,
        missing_field: str,
    ):
        payload = dict(unique_user_payload)
        payload.pop(missing_field)

        resp = api.post("/auth/register", json=payload)

        assert resp.status_code == 403
        assert resp.json.get("success") is False
        assert resp.json.get("message") == "Email, password and name are required fields"
