import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from data import TestBunData, TestIngredientData


@pytest.fixture
def test_burger():
    burger = Burger()
    return burger


@pytest.fixture
def test_bun():
    bun = Bun(TestBunData.name, TestBunData.price)
    return bun


@pytest.fixture
def test_ingredient():
    ingredient = Ingredient(TestIngredientData.ingredient_type, TestIngredientData.name, TestIngredientData.price)
    return ingredient


@pytest.fixture
def test_database():
    database = Database()
    return database