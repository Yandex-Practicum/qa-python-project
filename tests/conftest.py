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
    ingredient.get_price.return_value = 100
    return ingredient


@pytest.fixture
def mock_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 150
    return ingredient


@pytest.fixture
def mock_ingredient():
    def _create_mock(ingredient_type, name, price):
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        return ingredient
    return _create_mock