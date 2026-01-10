from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def bun():
    bun = Bun('Bulka', 50)
    return bun


@pytest.fixture()
def burger():
    burger = Burger()
    return burger


@pytest.fixture()
def mock_bun():
    mock_bun = Mock(Bun)
    mock_bun.get_name.return_value = 'Булка'
    mock_bun.get_price.return_value = 55
    return mock_bun


@pytest.fixture()
def mock_filling():
    mock_filling = Mock(Ingredient)
    mock_filling.get_name.return_value = 'meteor'
    mock_filling.get_price.return_value = 150
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_filling


@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock(Ingredient)
    mock_sauce.get_name.return_value = 'cheese'
    mock_sauce.get_price.return_value = 160
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_sauce


@pytest.fixture()
def filling():
    filling = Ingredient(INGREDIENT_TYPE_FILLING, 'potato', 170)
    return filling


@pytest.fixture()
def sauce():
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, 'island', 180)
    return sauce
