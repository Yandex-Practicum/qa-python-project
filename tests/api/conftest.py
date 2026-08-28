import warnings

import pytest
import requests

from api_client import StellarBurgersApi
from data import generate_user_data


@pytest.fixture(scope="session")
def api_client():
    client = StellarBurgersApi()
    yield client
    client.close()


@pytest.fixture
def user_factory(api_client):
    created_tokens = []

    def create_user(payload=None):
        user_data = payload or generate_user_data()
        response = api_client.create_user(user_data)

        if response.status_code == 200:
            token = response.json().get("accessToken")
            if token:
                created_tokens.append(token)

        return user_data, response

    yield create_user

    for token in created_tokens:
        try:
            api_client.delete_user(token)
        except requests.RequestException as error:
            warnings.warn(
                f"Не удалось удалить тестового пользователя: {error}",
                RuntimeWarning,
            )


@pytest.fixture
def registered_user(user_factory):
    payload, response = user_factory()
    assert response.status_code == 200, response.text

    response_body = response.json()
    return {
        "payload": payload,
        "access_token": response_body["accessToken"],
    }


@pytest.fixture(scope="session")
def ingredient_ids(api_client):
    response = api_client.get_ingredients()
    assert response.status_code == 200, response.text

    response_body = response.json()
    assert response_body["success"] is True
    assert len(response_body["data"]) >= 2
    return [ingredient["_id"] for ingredient in response_body["data"][:2]]
