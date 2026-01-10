
from unittest.mock import Mock
import pytest

from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE
from helpers import *


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = bun_name
    mock_bun.price = bun_price

    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = ingredient_name
    mock_ingredient.price = ingredient_price

    return mock_ingredient


@pytest.fixture(scope='function')
def mock_add_ingredients(mock_ingredient):
    new_ingredient = Burger()

    new_ingredient.add_ingredient(mock_ingredient)
    new_ingredient.add_ingredient(mock_ingredient)

    return new_ingredient
