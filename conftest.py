import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import bun_name


@pytest.fixture
def bun_object():
    return Bun(bun_name, 1.5)


@pytest.fixture
def ingredient_object_1():
    return Ingredient(INGREDIENT_TYPE_SAUCE, 'BBQ', 350.0)


@pytest.fixture
def ingredient_object_2():
    return Ingredient(INGREDIENT_TYPE_FILLING, 'колбаска', 200.0)


@pytest.fixture
def ingredient_object_3():
    return Ingredient(INGREDIENT_TYPE_FILLING, 'сыр', 100.0)


@pytest.fixture
def burger_object():
    return Burger()


@pytest.fixture
def database_object():
    return Database

