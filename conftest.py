import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from data import Data


@pytest.fixture()
def new_bun():
    bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
    return bun


@pytest.fixture()
def new_burger():
    burger = Burger()
    return burger


@pytest.fixture()
def new_ingredient():
    ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
    return ingredient


@pytest.fixture()
def new_database():
    database = Database()
    return database
