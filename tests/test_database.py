import pytest
from praktikum.database import Database

class TestDatabase:

    def test_database_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) > 0
        assert buns[0].get_name() is not None

    def test_database_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0
        assert ingredients[0].get_name() is not None
