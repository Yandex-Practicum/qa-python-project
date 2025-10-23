import pytest

from unittest.mock import patch, Mock
from data.test_data import BUN_VALID_NAME, BUN_VALID_FLOAT_PRICE, INGREDIENT_TYPE_VALID, INGREDIENT_NAME_VALID, \
    INGREDIENT_PRICE_VALID
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    return Bun(BUN_VALID_NAME, BUN_VALID_FLOAT_PRICE)

@pytest.fixture
def mock_and_add_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_TYPE_VALID
    mock_ingredient.name = INGREDIENT_NAME_VALID
    mock_ingredient.price = INGREDIENT_PRICE_VALID
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_VALID
    mock_ingredient.get_name.return_value = INGREDIENT_NAME_VALID
    mock_ingredient.get_price.return_value = INGREDIENT_PRICE_VALID

    burger = Burger()
    burger.add_ingredient(mock_ingredient)

    return burger, mock_ingredient

@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_VALID, INGREDIENT_NAME_VALID, INGREDIENT_PRICE_VALID)
