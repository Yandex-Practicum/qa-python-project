from typing import List

import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def mok_bun():
    bun = Mock(spec=Bun)
    bun.name = 'sdoba'
    bun.price = 111
    return bun


@pytest.fixture
def mok_ingredient(mok_bun):
    ingredient = Mock(spec=Ingredient)
    ingredient.set_buns = mok_bun
    ingredient.add_ingredient = ingredient
    ingredient.remove_ingredient = ingredient
    ingredient.move_ingredient = ingredient
    ingredient.get_price = mok_bun
    return ingredient


@pytest.fixture
def mock_ingredients(mok_ingredient):
    ingredients = Mock(spec=Burger)
    ingredients = List[mok_ingredient]
    return ingredients


@pytest.fixture
def burger():
    return Burger()
