import pytest
from unittest.mock import MagicMock
from bun import Bun
from ingredient import Ingredient
from burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    mock_bun = MagicMock(spec=Bun)
    mock_bun.get_price.return_value = 50.0
    mock_bun.get_name.return_value = "Sesame Bun"
    return mock_bun


@pytest.fixture
def ingredient():
    mock_ingredient = MagicMock(spec=Ingredient)
    mock_ingredient.get_price.return_value = 20.0
    mock_ingredient.get_name.return_value = "Lettuce"
    mock_ingredient.get_type.return_value = "vegetable"
    return mock_ingredient
