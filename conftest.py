import pytest

from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "big_bun"
    bun.get_price.return_value = 111
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = 121
    ingredient.get_name.return_value = "x_ingredient"
    ingredient.get_type.return_value = "FILLING"
    return ingredient
