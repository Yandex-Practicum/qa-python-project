from database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_database_lists():
    db = Database()
    buns = db.available_buns()
    ingredients = db.available_ingredients()

    assert isinstance(buns, list)
    assert isinstance(ingredients, list)
    assert len(buns) == 3
    assert len(ingredients) == 6
