import os
import sys

# make src importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import pytest
import allure

from stellar_burgers.api_client import StellarApiClient
from stellar_burgers.data_builders import build_unique_user


@pytest.fixture(scope="session")
def api() -> StellarApiClient:
    return StellarApiClient()


@pytest.fixture
def unique_user_payload():
    user = build_unique_user()
    return {"email": user.email, "password": user.password, "name": user.name}


@pytest.fixture
def registered_user(api: StellarApiClient, unique_user_payload):
    """Creates a user before test and deletes it after test."""
    with allure.step("Register user"):
        resp = api.post("/auth/register", json=unique_user_payload)
    assert resp.status_code == 200, f"Failed to register user: {resp.status_code} {resp.json}"
    assert resp.json.get("success") is True

    access_token = resp.json.get("accessToken")
    refresh_token = resp.json.get("refreshToken")

    yield {
        "payload": unique_user_payload,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    # cleanup (best-effort)
    if access_token:
        with allure.step("Delete user (cleanup)"):
            api.delete("/auth/user", headers={"Authorization": access_token})
