import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50
    return ingredient

@pytest.fixture
def mock_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 100
    return ingredient
