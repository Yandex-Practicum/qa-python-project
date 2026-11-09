import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black_bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def make_ingredient():
    def _make(name="dinosaur", price=50, ingredient_type="FILLING"):
        ingredient = Mock()
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        ingredient.get_type.return_value = ingredient_type
        return ingredient
    return _make