import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def buns(request):
    bun_name = 'black bun'
    bun_price = 100
    buns = Bun(bun_name, bun_price)
    return buns


@pytest.fixture
def ingredient1():
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'chili sauce', 300)
    return ingredient1

@pytest.fixture
def ingredient2():
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    return ingredient2

@pytest.fixture
def ingredient3():
    ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
    return ingredient3

@pytest.fixture
def burgers():
    burgers = Burger()
    return burgers

@pytest.fixture
def db():
    db = Database()
    return db
