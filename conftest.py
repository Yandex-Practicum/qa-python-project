import pytest
import random

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture(scope='function')
def create_bun_mock():
    db = Database()
    bun = db.buns[random.randint(0,2)]
    mock_bun = Mock()
    mock_bun.name = bun.name
    mock_bun.price = bun.price
    return mock_bun

@pytest.fixture(scope='function')
def create_ingredient_mock():
    db = Database()
    ingredient = db.ingredients[random.randint(0,5)]
    mock_ingredient = Mock()
    mock_ingredient.name = ingredient.name
    mock_ingredient.price = ingredient.price
    mock_ingredient.type = ingredient.type
    return mock_ingredient

@pytest.fixture(scope='function')
def create_test_burger():
    db = Database()
    bun = db.buns[random.randint(0,2)]
    ingredient_1 = db.ingredients[random.randint(0,2)]
    ingredient_2 = db.ingredients[random.randint(3,5)]
    burger = Burger()
    burger.set_buns(bun=bun)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    return burger, bun, ingredient_1, ingredient_2