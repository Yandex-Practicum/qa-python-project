import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import *

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'Марсианская Булка'
    bun.get_price.return_value = 5
    return bun

@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = 'Кеплерская Курочка'
    ingredient.get_price.return_value = 15
    return ingredient

@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = 'Юпитерский Соус'
    ingredient.get_price.return_value = 2
    return ingredient
