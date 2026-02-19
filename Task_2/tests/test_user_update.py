import allure
import pytest
from typing import Optional

from stellar_burgers.api_client import StellarApiClient
from tests.helpers import auth_header, random_email


@allure.feature("User")
@allure.story("Update user data")
class TestUserUpdate:
    @pytest.mark.parametrize(
        "field,new_value",
        [
            # Email must be unique on a shared stand.
            ("email", None),
            ("name", "Updated Name"),
            ("password", "UpdatedPassword123"),
        ],
    )
    def test_update_user_with_authorization_success(
        self,
        api: StellarApiClient,
        registered_user,
        field: str,
        new_value: Optional[str],
    ):
        token = registered_user["access_token"]
        value = random_email("updated") if field == "email" else new_value
        resp = api.patch("/auth/user", json={field: value}, headers=auth_header(token))

        assert resp.status_code == 200
        assert resp.json.get("success") is True
        assert resp.json.get("user") is not None

        if field in ("email", "name"):
            assert resp.json["user"].get(field) == value

    @pytest.mark.parametrize(
        "field,new_value",
        [
            ("email", "unauth_email@yandex.ru"),
            ("name", "Unauth Name"),
            ("password", "UnauthPassword123"),
        ],
    )
    def test_update_user_without_authorization_returns_401(
        self,
        api: StellarApiClient,
        field: str,
        new_value: str,
    ):
        resp = api.patch("/auth/user", json={field: new_value})

        assert resp.status_code == 401
        assert resp.json.get("success") is False
        assert resp.json.get("message") == "You should be authorised"
