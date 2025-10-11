import pytest
from unittest.mock import MagicMock

@pytest.fixture
def bun_mock():
    bun_mock = MagicMock()
    bun_mock.get_name.return_value = "Датская булка"
    bun_mock.get_price.return_value = 100
    return bun_mock

@pytest.fixture
def ingredient_mock_1():
    ingredient_mock = MagicMock()
    ingredient_mock.get_type.return_value = "Наполнитель"
    ingredient_mock.get_name.return_value = "Сосика"
    ingredient_mock.get_price.return_value = 300
    return ingredient_mock

@pytest.fixture
def ingredient_mock_2():
    ingredient_mock = MagicMock()
    ingredient_mock.get_type.return_value = "Наполнитель"
    ingredient_mock.get_name.return_value = "Огурчики"
    ingredient_mock.get_price.return_value = 200
    return ingredient_mock
