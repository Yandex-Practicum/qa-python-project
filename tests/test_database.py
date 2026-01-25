import pytest
from Diplom_1.praktikum.database import Database
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.bun import Bun


def test_database_init():
    database = Database()
    assert isinstance(database.buns, list)
    assert isinstance(database.ingredients, list)


def test_database_available_buns():
    database = Database()
    buns = database.available_buns()
    assert len(buns) == 3
    assert all(isinstance(bun, Bun) for bun in buns)


def test_database_available_ingredients():
    database = Database()
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
