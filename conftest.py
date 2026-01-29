import pytest

from .praktikum.bun import Bun
from .praktikum.burger import Burger
from .praktikum.database import Database
from .praktikum.ingredient import Ingredient
from .tests.data import (ingredient_2_name, ingredient_2_price,
                         ingredient_2_type, ingredient_name, ingredient_price,
                         ingredient_type, test_bun_2_name, test_bun_2_price,
                         test_bun_name, test_bun_price)


@pytest.fixture
def bun():
    return (Bun(test_bun_name, test_bun_price))


@pytest.fixture
def bun_2():
    return (Bun(test_bun_2_name, test_bun_2_price))


@pytest.fixture
def burger():
    return (Burger())


@pytest.fixture
def ingredient():
    return (Ingredient(ingredient_type, ingredient_name, ingredient_price))


@pytest.fixture
def ingredient_2():
    return (Ingredient(ingredient_2_type,
                       ingredient_2_name,
                       ingredient_2_price))


@pytest.fixture
def burger_full(burger, bun, ingredient, ingredient_2):
    burger.bun = bun
    burger.ingredients = [ingredient, ingredient_2]

    return burger


@pytest.fixture
def database(bun, bun_2, ingredient, ingredient_2):
    db = Database()
    db.buns = [bun, bun_2]
    db.ingredients = [ingredient, ingredient_2]
    return db
