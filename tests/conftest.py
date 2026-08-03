import pytest
from unittest.mock import Mock

from burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "big bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "chilli sauce"
    ingredient.get_price.return_value = 50
    return ingredient