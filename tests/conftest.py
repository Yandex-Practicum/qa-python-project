import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import BUN_NAME, BUN_PRICE, INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE, FILLING_NAME, FILLING_TYPE, FILLING_PRICE


@pytest.fixture
def bun_mock():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def ingredient_mock():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE
    ingredient.get_name.return_value = INGREDIENT_NAME
    ingredient.get_price.return_value = INGREDIENT_PRICE
    return ingredient


@pytest.fixture
def filling_mock():
    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = FILLING_TYPE
    filling.get_name.return_value = FILLING_NAME
    filling.get_price.return_value = FILLING_PRICE
    return filling