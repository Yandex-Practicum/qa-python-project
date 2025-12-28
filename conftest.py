import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.resolve()))

import pytest
import data
import generators
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture()
def mock_create_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = data.DataBun.BUN_NAME
    mock_bun.get_price.return_value = data.DataBun.BUN_PRICE
    return mock_bun

@pytest.fixture()
def mock_create_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = generators.generate_word()
    mock_ingredient.get_name.return_value = generators.generate_word()
    mock_ingredient.get_price.return_value = generators.generate_price()
    return mock_ingredient

@pytest.fixture()
def mock_ingredients():
    ingredients = []
    for i in range(data.DataIngredient.QUANTITY_INGREDIENT):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = f"type_{i}"
        mock_ingredient.get_name.return_value = f"ingredient_{i}"
        mock_ingredient.get_price.return_value = 10 * (i+1)
        ingredients.append(mock_ingredient)
    return ingredients

@pytest.fixture()
def prepared_burger(mock_create_bun, mock_ingredients):
    burger = Burger()
    burger.bun = mock_create_bun
    for ingredient in mock_ingredients:
        burger.add_ingredient(ingredient)
    return burger