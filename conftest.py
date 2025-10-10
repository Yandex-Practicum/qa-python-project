from unittest.mock import Mock

import pytest

import data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun(data.NAME_BUN, data.PRICE_BUN)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(data.TYPE_INGREDIENT, data.NAME_INGREDIENT, data.PRICE_INGREDIENT)
    return ingredient

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def database():
    database = Database()
    return database

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.price = data.PRICE_BUN
    mock_bun.name = data.NAME_BUN
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.price = data.PRICE_INGREDIENT
    mock_ingredient.name = data.NAME_INGREDIENT
    return mock_ingredient

