import pytest


from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.data import FILLING, SAUCE, BUN_WITH_INDEX


class TestDatabase:
    def test_database_has_three_buns(self):
        db = Database()
        assert len(db.available_buns()) == 3

    def test_database_has_six_ingredients(self):
        db = Database()
        assert len(db.available_ingredients()) == 6

    @pytest.mark.parametrize("index, name, price", BUN_WITH_INDEX)
    def test_available_buns_content(self, index, name, price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].get_name() == name
        assert buns[index].get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", FILLING + SAUCE)
    def test_available_ingredients_content(self, ingredient_type, name, price):
        db = Database()
        ingredients = db.available_ingredients()
        assert any(
            ingredient.get_type() == ingredient_type
            and ingredient.get_name() == name
            and ingredient.get_price() == price
            for ingredient in ingredients
        )

    def test_database_returns_buns_as_bun_objects(self):
        db = Database()
        buns = db.available_buns()
        assert all(isinstance(b, Bun) for b in buns)

    def test_database_returns_ingredients_as_ingredient_objects(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert all(isinstance(i, Ingredient) for i in ingredients)