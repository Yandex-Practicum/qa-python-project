import pytest
from unittest.mock import Mock

from burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "green bun"
    bun.get_price.return_value = 110
    return bun


@pytest.fixture
def mock_ingredient1():
    ingredient = Mock()
    ingredient.get_name.return_value = "bbq"
    ingredient.get_price.return_value = 140
    ingredient.get_type.return_value = 'SAUCE'
    return ingredient


@pytest.fixture
def mock_ingredient2():
    ingredient = Mock()
    ingredient.get_name.return_value = "cheese"
    ingredient.get_price.return_value = 170
    ingredient.get_type.return_value = 'FILLING'
    return ingredient


@pytest.fixture
def prepared_burger(burger, mock_bun, mock_ingredient1, mock_ingredient2):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient1)
    burger.add_ingredient(mock_ingredient2)
    return burger
