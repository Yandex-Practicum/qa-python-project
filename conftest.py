import pytest
from unittest.mock import Mock


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = 'SAUCE'
    ingredient.get_name.return_value = 'hot sauce'
    ingredient.get_price.return_value = 50
    return ingredient
