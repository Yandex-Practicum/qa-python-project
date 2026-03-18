import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from unittest.mock import Mock, patch
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import SPICY_SAUCE, TEST_FILLING, TEST_SAUCE, STONE_BUN, BLACK_BUN

# Фикстуры для моков

@pytest.fixture
def bun_mock():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = STONE_BUN['name']
    mock_bun.get_price.return_value = STONE_BUN['price']
    return mock_bun

@pytest.fixture
def ingredient_mock():
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = TEST_SAUCE['name']
    mock_ingredient.get_price.return_value = TEST_SAUCE['price']
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient

@pytest.fixture
def ingredient_mock_filling():
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = TEST_FILLING['name']
    mock_ingredient.get_price.return_value = TEST_FILLING['price']
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_ingredient

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, SPICY_SAUCE['name'], SPICY_SAUCE['price'])

@pytest.fixture
def burger():
    return Burger()


