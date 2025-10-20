import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns_returns_expected_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(b, Bun) for b in buns)
        assert {b.get_name() for b in buns} == {"black bun", "white bun", "red bun"}

    def test_available_ingredients_returns_expected_types_and_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(i, Ingredient) for i in ingredients)

        types = [i.get_type() for i in ingredients]
        sauce_count = sum(1 for t in types if t == INGREDIENT_TYPE_SAUCE)
        filling_count = sum(1 for t in types if t == INGREDIENT_TYPE_FILLING)

        assert sauce_count == 3
        assert filling_count == 3
