import pytest

from bun import Bun
from ingredient import Ingredient
from database import Database

@pytest.fixture
def create_bun(name, price):
    bun = Bun(name, price)
    return bun

@pytest.fixture
def create_ingredient(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient

@pytest.fixture
def new_database():
    new_database = Database()
    return new_database








