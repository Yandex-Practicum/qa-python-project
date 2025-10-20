
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import TestData

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = TestData.mock_bun_name
    mock_bun.get_price.return_value = TestData.mock_bun_price
    return mock_bun

@pytest.fixture
def mock_ingredient_sauce():
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = TestData.mock_sauce_name
    mock_ingredient.get_price.return_value = TestData.mock_sauce_price
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient

@pytest.fixture
def mock_ingredient_filling():
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = TestData.mock_filling_name
    mock_ingredient.get_price.return_value = TestData.mock_filling_price
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_ingredient

@pytest.fixture
def mock_ingredients():
    ingredients = []
    for i in range(3):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = f"ingredient_{i}"
        mock_ingredient.get_price.return_value = 25.0 * (i + 1)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE if i % 2 == 0 else INGREDIENT_TYPE_FILLING
        ingredients.append(mock_ingredient)
    return ingredients