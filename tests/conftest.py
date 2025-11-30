import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import *
from data import *


@pytest.fixture
def mock_bun():  # Мок для булочки
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BUN_DATA["name"]
    bun.get_price.return_value = BUN_DATA["price"]
    return bun


@pytest.fixture
def mock_ingredient_sauce():  # Мок для соуса
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_SAUCE_DATA["type"]
    ingredient.get_name.return_value = INGREDIENT_SAUCE_DATA["name"]
    ingredient.get_price.return_value = INGREDIENT_SAUCE_DATA["price"]
    return ingredient


@pytest.fixture
def mock_ingredient_filling():  # Мок для начинки
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_FILLING_DATA["type"]
    ingredient.get_name.return_value = INGREDIENT_FILLING_DATA["name"]
    ingredient.get_price.return_value = INGREDIENT_FILLING_DATA["price"]
    return ingredient


@pytest.fixture
def mock_ingredients(mock_ingredient_sauce, mock_ingredient_filling):
    return {
        INGREDIENT_TYPE_SAUCE: mock_ingredient_sauce,
        INGREDIENT_TYPE_FILLING: mock_ingredient_filling,
    }
