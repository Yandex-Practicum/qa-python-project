import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredient_sauce():
    ing = Mock()
    ing.get_type.return_value = "SAUCE"
    ing.get_name.return_value = "hot sauce"
    ing.get_price.return_value = 50
    return ing


@pytest.fixture
def ingredient_filling():
    ing = Mock()
    ing.get_type.return_value = "FILLING"
    ing.get_name.return_value = "cutlet"
    ing.get_price.return_value = 200
    return ing