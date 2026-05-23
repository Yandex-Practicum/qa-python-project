import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_available_buns_returns_list_of_buns(self):
        db = Database()
        buns = db.available_buns()
        assert all(isinstance(b, Bun) for b in buns)

    def test_available_buns_count(self):
        db = Database()
        assert len(db.available_buns()) == 3

    def test_available_ingredients_returns_list_of_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert all(isinstance(i, Ingredient) for i in ingredients)

    def test_available_ingredients_count(self):
        db = Database()
        assert len(db.available_ingredients()) == 6

    @pytest.mark.parametrize("ingredient_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_available_ingredients_contain_type(self, ingredient_type):
        db = Database()
        types = [i.get_type() for i in db.available_ingredients()]
        assert ingredient_type in types
        