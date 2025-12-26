from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def bun():
    bun = Bun('Briosh', 100)
    return bun


@pytest.fixture()
def burger():
    burger = Burger()
    return burger


@pytest.fixture()
def mock_bun():
    mock_bun = Mock(Bun)
    mock_bun.get_name.return_value = 'briosh'
    mock_bun.get_price.return_value = 75
    return mock_bun


@pytest.fixture()
def mock_topping():
    mock_topping = Mock(Ingredient)
    mock_topping.get_name.return_value = 'salad'
    mock_topping.get_price.return_value = 30
    mock_topping.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_topping


@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock(Ingredient)
    mock_sauce.get_name.return_value = 'onion'
    mock_sauce.get_price.return_value = 20
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_sauce


@pytest.fixture()
def topping():
    topping = Ingredient(INGREDIENT_TYPE_FILLING, 'potato', 140)
    return topping


@pytest.fixture()
def sauce():
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, 'ketchup', 80)
    return sauce
