import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100
    return ingredient