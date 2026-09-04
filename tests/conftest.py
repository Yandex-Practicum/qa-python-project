from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from tests.data import BURGER_BUN, BURGER_INGREDIENTS


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BURGER_BUN[0]
    bun.get_price.return_value = BURGER_BUN[1]
    return bun


@pytest.fixture
def ingredient_mocks():
    mocks = []
    for ingredient_type, name, price in BURGER_INGREDIENTS:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        mocks.append(ingredient)
    return mocks


@pytest.fixture
def database():
    return Database()
