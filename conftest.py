import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
import data

@pytest.fixture()
def bun():
    bun = Bun(data.BUN_NAME, data.BUN_PRICE)
    return bun

@pytest.fixture()
def burger():
    burger = Burger()
    return burger

@pytest.fixture()
def ingredient():
    ingredient = Ingredient(data.INGR_TYPE, data.INGR_NAME, data.INGR_PRICE)
    return ingredient

@pytest.fixture()
def database():
    database = Database()
    return database