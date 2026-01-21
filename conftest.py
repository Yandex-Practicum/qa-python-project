import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Фикстура для булки
@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "булка"
    mock.get_price.return_value = 200
    return mock


# Фикстура для ингредиента типа соус
@pytest.fixture()
def mock_sauce():
    mock = Mock()
    mock.get_name.return_value = "горячий соус"
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


# Фикстура для ингредиента типа начинка
@pytest.fixture()
def mock_filling():
    mock = Mock()
    mock.get_name.return_value = "котлета"
    mock.get_price.return_value = 150
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock


# фикстура для объекта database
@pytest.fixture()
def mock_database():
    db = Database()
    return db
