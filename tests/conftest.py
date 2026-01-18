import pytest
from unittest.mock import Mock

from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_name.return_value = "salsa"
    sauce.get_price.return_value = 50
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce


@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_name.return_value = "chicken"
    filling.get_price.return_value = 150
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return filling
