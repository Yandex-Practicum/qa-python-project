import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture(scope='function')
def bun():
    bun = Bun('crazy bun', 999)
    return bun


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "crazy sauce", 555)
    return ingredient


@pytest.fixture(scope='function')
def database():
    database = Database()
    return database
