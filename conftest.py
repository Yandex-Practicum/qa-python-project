import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Основные фикстуры
@pytest.fixture
def bun():
    return Bun("test bun", 100.0)


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def database():
    return Database()


# Моки для тестирования Burger
@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "test bun"
    mock.get_price.return_value = 100.0
    return mock


@pytest.fixture
def mock_ingredient_sauce():
    mock = Mock()
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock.get_name.return_value = "hot sauce"
    mock.get_price.return_value = 50.0
    return mock


@pytest.fixture
def mock_ingredient_filling():
    mock = Mock()
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock.get_name.return_value = "cutlet"
    mock.get_price.return_value = 80.0
    return mock
