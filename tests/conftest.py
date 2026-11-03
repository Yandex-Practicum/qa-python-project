from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 100.0
    return ingredient


@pytest.fixture
def burger_with_bun(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    return burger