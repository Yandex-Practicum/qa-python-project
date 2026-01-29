from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_ingredients_sauce():
    mock_ingredient_sauce = Mock(Ingredient)
    mock_ingredient_sauce.get_price.return_value = 0.5
    mock_ingredient_sauce.get_name.return_value = "ketchup"
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient_sauce


@pytest.fixture()
def mock_ingredients_sauce_filling():
    mock_ingredient_filling = Mock(Ingredient)
    mock_ingredient_filling.get_price.return_value = 1.0
    mock_ingredient_filling.get_name.return_value = "cheese"
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_ingredient_filling


@pytest.fixture()
def mock_bun():
    mock_bun = Mock(Bun)
    mock_bun.get_price.return_value = 1.5
    mock_bun.get_name.return_value = "Sesame"
    return mock_bun
