import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import constants

@pytest.fixture
def bun():
    bun = Bun(constants.PUDGE_BUN, 100)
    return bun

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, constants.MEAT_SAUCE, 100)
    return ingredient

@pytest.fixture
def database():
    database = Database()
    return database



