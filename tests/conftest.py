from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from helpers.api import register_user, delete_user, get_ingredients
from helpers.data_generators import generate_unique_email


@pytest.fixture
def unique_user_data():
    return {
        "email": generate_unique_email(),
        "password": "Password123!",
        "name": "Test User"
    }


@pytest.fixture
def created_user(unique_user_data):
    """
    Создаёт пользователя и возвращает его данные + токен.
    После теста удаляет пользователя.
    """
    response = register_user(
        unique_user_data["email"],
        unique_user_data["password"],
        unique_user_data["name"]
    )
    assert response.status_code == 200
    data = response.json()
    yield {
        "email": unique_user_data["email"],
        "password": unique_user_data["password"],
        "name": unique_user_data["name"],
        "access_token": data["accessToken"],
        "refresh_token": data["refreshToken"]
    }
    # Очистка после теста
    delete_user(data["accessToken"])


@pytest.fixture(scope="session")
def ingredients():
    """Получаем список ингредиентов один раз за всю сессию"""
    response = get_ingredients()
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    return data["data"]