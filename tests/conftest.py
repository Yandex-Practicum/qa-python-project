import random
import pytest
from praktikum.burger import Burger
from praktikum.database import Database

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def database():
    database = Database()
    return database

@pytest.fixture(scope='function')
def ready_burger():
    database = Database()
    burger = Burger()
    burger.set_buns(random.choice(database.available_buns()))
    for ingredient in database.available_ingredients():
        burger.add_ingredient(ingredient)
    return burger