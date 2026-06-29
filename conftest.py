import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun("white bun", 200)


@pytest.fixture
def ingredient1():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

@pytest.fixture
def ingredient2():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)

@pytest.fixture
def ingredient3():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)

@pytest.fixture
def data():
    return Database()