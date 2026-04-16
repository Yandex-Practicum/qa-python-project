from unittest.mock import Mock

import pytest

import data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def bun():
    bun = Bun(data.bun_name, data.bun_price)
    return bun


@pytest.fixture()
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, data.ingredient_name, data.ingredient_price)
    return ingredient


@pytest.fixture()
def ingredient_requested_type(request):
    ingredient_type = request.param
    ingredient = Ingredient(ingredient_type, data.ingredient_name, data.ingredient_price)
    return ingredient


@pytest.fixture()
def burger():
    burger = Burger()
    return burger


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = data.bun_name
    mock_bun.get_price.return_value = data.bun_price
    return mock_bun


@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = data.ingredient_name
    mock_ingredient.get_price.return_value = data.ingredient_price
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient


@pytest.fixture()
def database():
    database = Database()
    return database
