from conftest import mok_bun, mok_ingredient, burger
from praktikum.database import Database


def test_available_buns(burger, mok_bun):
    burger.set_buns(mok_bun)
    database = Database()
    database.available_buns()
    assert mok_bun not in database.buns


def test_available_ingredients(burger, mok_ingredient):
    burger.add_ingredient(mok_ingredient)
    database = Database()
    database.available_ingredients()
    assert mok_ingredient not in database.ingredients
