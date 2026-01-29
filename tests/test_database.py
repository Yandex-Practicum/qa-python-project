import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import DATABASE_BUNS_EXPECTED, DATABASE_INGREDIENTS_EXPECTED


@pytest.fixture
def database():
    return Database()


def test_available_buns(database):
    buns = database.available_buns()
    assert len(buns) == DATABASE_BUNS_EXPECTED["count"]
    assert all(isinstance(bun, Bun) for bun in buns)
    assert buns[0].get_name() == DATABASE_BUNS_EXPECTED["first_name"]
    assert buns[0].get_price() == DATABASE_BUNS_EXPECTED["first_price"]


def test_available_ingredients(database):
    ingredients = database.available_ingredients()
    assert len(ingredients) == DATABASE_INGREDIENTS_EXPECTED["count"]
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    assert ingredients[0].get_name() == DATABASE_INGREDIENTS_EXPECTED["first_name"]
    assert ingredients[0].get_type() == DATABASE_INGREDIENTS_EXPECTED["first_type"]
