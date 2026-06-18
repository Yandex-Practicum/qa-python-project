import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from unittest.mock import Mock
import praktikum.ingredient_types as ingredient_types
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def database():
    database = Database()
    return database

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'black bun'
    mock_bun.get_price.return_value = 100.0
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = 'cheese'
    mock_ingredient.get_price.return_value = 70.0
    mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    return mock_ingredient

@pytest.fixture
def ingredient():
    return Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "cheese", 70.0)

@pytest.fixture
def bun():
    return Bun('black bun', 100.0)