import pytest
import requests
import allure
from requests.exceptions import ConnectionError, Timeout
from tests import urls
from tests.data_generator import DataGenerator


@pytest.fixture(scope="session")
def api_available():
    """Проверяет доступность API перед запуском тестов"""
    try:
        with allure.step("Проверить доступность API"):
            response = requests.get(f"{urls.BASE_URL}/ingredients", timeout=5)
            response.raise_for_status()
        return True
    except (ConnectionError, Timeout):
        pytest.skip("API недоступно, пропускаем тесты")
    except Exception:
        pytest.skip("Проблема с API, пропускаем тесты")


@pytest.fixture
def registered_user(api_available):
    """Фикстура для создания и удаления зарегистрированного пользователя"""
    generator = DataGenerator()
    user_data = generator.generate_user_data()

    try:
        with allure.step("Создать тестового пользователя"):
            response = requests.post(
                f"{urls.BASE_URL}/auth/register",
                json=user_data,
                timeout=10
            )
            response.raise_for_status()
            token = response.json()["accessToken"]

        yield {
            "email": user_data["email"],
            "password": user_data["password"],
            "name": user_data["name"],
            "token": token
        }

    finally:
        # Пост-условие: удаление пользователя без allure.step
        try:
            if 'token' in locals():
                headers = {"Authorization": token}
                requests.delete(
                    f"{urls.BASE_URL}/auth/user",
                    headers=headers,
                    timeout=10
                )
        except Exception:
            pass


@pytest.fixture
def temporary_user(api_available):
    """Фикстура для временного пользователя, который будет удален после теста"""
    generator = DataGenerator()
    user_data = generator.generate_user_data()

    response = requests.post(
        f"{urls.BASE_URL}/auth/register",
        json=user_data,
        timeout=10
    )
    response.raise_for_status()
    token = response.json()["accessToken"]

    user_info = {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "token": token
    }

    yield user_info

    # Пост-условие: удаление пользователя
    try:
        headers = {"Authorization": token}
        requests.delete(
            f"{urls.BASE_URL}/auth/user",
            headers=headers,
            timeout=10
        )
    except Exception:
        pass


@pytest.fixture
def ingredient_data(api_available):
    """Фикстура для получения данных об ингредиентах"""
    try:
        with allure.step("Получить данные об ингредиентах"):
            response = requests.get(f"{urls.BASE_URL}/ingredients", timeout=10)
            response.raise_for_status()
            ingredients = response.json()["data"]
        return ingredients
    except (ConnectionError, Timeout) as e:
        pytest.skip(f"API недоступно: {e}")
    except Exception as e:
        pytest.skip(f"Ошибка при получении ингредиентов: {e}")
