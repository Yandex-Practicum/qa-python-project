import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'Краторная булка N-200i'
    bun.get_price.return_value = 1255
    return bun


@pytest.fixture
def mock_ingredient1():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = 'Говяжий метеорит (отбивная)'
    ingredient.get_price.return_value = 3000
    return ingredient


@pytest.fixture
def mock_ingredient2():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = 'Соус Spicy-X'
    ingredient.get_price.return_value = 90
    return ingredient