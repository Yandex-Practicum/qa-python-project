from unittest.mock import Mock

import pytest

from burger import Burger
from ingredient import Ingredient

from tests.test_data import (
    BUN_NAME,
    BUN_PRICE,
    INGREDIENT_NAME,
    INGREDIENT_PRICE,
    INGREDIENT_TYPE,
)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE
    ingredient.get_name.return_value = INGREDIENT_NAME
    ingredient.get_price.return_value = INGREDIENT_PRICE
    return ingredient


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)
