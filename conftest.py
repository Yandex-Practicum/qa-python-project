from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from generators import *

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = mock_bun_name
    mock_bun.price = mock_bun_price
    return mock_bun

@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = mock_ingredient_name
    mock_ingredient.price = mock_ingredient_price
    return mock_ingredient
