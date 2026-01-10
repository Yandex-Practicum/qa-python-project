import pytest

from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.bun import Bun


@pytest.fixture
def bun():
    bun = Bun('black bun', 100)
    return bun

@pytest.fixture
def ingredient():
    ing = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 10)
    return ing

@pytest.fixture
def burger():
    burger = Burger()
    return burger