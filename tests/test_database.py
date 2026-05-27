import pytest
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert isinstance(buns, list)

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert isinstance(ingredients, list)