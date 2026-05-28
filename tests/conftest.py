import pytest
from unittest.mock import Mock

from burger import Burger
from bun import Bun
from ingredient import Ingredient
from data import (
    BUN_NAME,
    BUN_PRICE,
    SAUCE_TYPE,
    SAUCE_NAME,
    SAUCE_PRICE,
)

@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    return Bun(BUN_NAME, BUN_PRICE)


@pytest.fixture
def ingredient():
    return Ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = SAUCE_TYPE
    ingredient.get_name.return_value = SAUCE_NAME
    ingredient.get_price.return_value = SAUCE_PRICE
    return ingredient