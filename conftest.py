import pytest
from data import Data
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "mock bun"
    bun.get_price.return_value = 50
    return bun

@pytest.fixture
def mock_ingredients():
    ingredients = []
    for value in Data.MOCK_INGREDIENTS:
        ingredient = Mock()
        ingredient.get_type.return_value = value[0]
        ingredient.get_name.return_value = value[1]
        ingredient.get_price.return_value = value[2]
        ingredients.append(ingredient)
    return ingredients
