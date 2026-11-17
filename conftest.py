import pytest
from unittest.mock import Mock 
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def burger():
    return Burger()

@pytest.fixture()
def mock_bun():
    bun = Mock()
    bun.get_name.return_value= 'Краторная булка N-200i'
    bun.get_price.return_value = 1255
    return bun

@pytest.fixture()
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value='Хрустящие минеральные кольца'
    ingredient.get_price.return_value = 300
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient

@pytest.fixture()
def mock_ingredient_1():
    ingredient_1 = Mock()
    ingredient_1.get_name.return_value= 'Spicy-X'
    ingredient_1.get_price.return_value = 90
    ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient_1

