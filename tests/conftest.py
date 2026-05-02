import pytest 
from praktikum.burger import Burger
from unittest.mock import MagicMock

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_price.return_value = 200.0
    bun.get_name.return_value = "toasted bun"
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 80.0
    ingredient.get_name.return_value = "cheddar slice"
    ingredient.get_type.return_value = "FILLING"
    return ingredient