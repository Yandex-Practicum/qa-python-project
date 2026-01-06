import pytest
from unittest.mock import patch

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_buns_type(self):
        db = Database()
        buns = db.available_buns()
        assert all(isinstance(b, Bun) for b in buns)

    def test_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_ingredients_type(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert all(isinstance(i, Ingredient) for i in ingredients)

    @pytest.mark.parametrize("ingredient_name", [
        "hot sauce", "sour cream", "chili sauce",
        "cutlet", "dinosaur", "sausage"])
    def test_ingredient_exists(self, ingredient_name):
        db = Database()
        ingredient = next(
            (i for i in db.available_ingredients() if i.get_name() == ingredient_name),
            None)
        assert ingredient is not None
        assert isinstance(ingredient, Ingredient)

    @pytest.mark.parametrize("bun_name", ["black bun", "white bun", "red bun"])
    def test_bun_exists(self, bun_name):
        db = Database()
        bun = next((b for b in db.available_buns() if b.get_name() == bun_name), None)
        assert bun is not None
        assert isinstance(bun, Bun)
