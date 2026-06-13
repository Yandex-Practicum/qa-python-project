import pytest
from praktikum.burger import Burger
from praktikum.database import Database
from helpers import create_mock_ingredient
from data import *

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def full_burger():
    """Полностью собранный бургер."""
    burger = Burger()
    bun = create_mock_ingredient("bun", TEST_BUN["name"], TEST_BUN["price"])
    sauce = create_mock_ingredient(**TEST_SAUCE)
    filling = create_mock_ingredient(**TEST_FILLING_1)

    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    return burger

