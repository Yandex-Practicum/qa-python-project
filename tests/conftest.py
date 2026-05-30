import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Black Bun"
    bun.get_price.return_value = 100.0
    return bun

@pytest.fixture
def mock_ingredient():
    def _mock_ingredient(ingredient_type, name, price):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        return ingredient
    return _mock_ingredient