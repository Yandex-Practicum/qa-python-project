import pytest
import sys
import os

# Добавляем корень проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data.test_data import (
    BUN_NAME, BUN_PRICE, BUN_NAME_2, BUN_PRICE_2,
    INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT_NAME_2, INGREDIENT_PRICE_2
)

@pytest.fixture
def bun():
    return Bun(BUN_NAME, BUN_PRICE)

@pytest.fixture
def burger_with_bun():
    bun = Bun(BUN_NAME, BUN_PRICE)
    burger = Burger()
    burger.set_buns(bun)
    return burger

@pytest.fixture
def burger_with_ingredients():
    bun = Bun(BUN_NAME, BUN_PRICE)
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
    ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_2, INGREDIENT_PRICE_2)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    burger.add_ingredient(ingredient_filling)
    return burger

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)

@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_2, INGREDIENT_PRICE_2)