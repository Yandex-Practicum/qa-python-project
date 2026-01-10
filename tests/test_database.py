import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def db():
    return Database()


class TestDatabase:

    # ---------- available_buns ----------
    def test_available_buns_returns_list(self, db):
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_elements_are_bun(self, db):
        buns = db.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_buns_not_empty(self, db):
        buns = db.available_buns()
        assert len(buns) > 0

    # ---------- available_ingredients ----------
    def test_available_ingredients_returns_list(self, db):
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_elements_are_ingredient(self, db):
        ingredients = db.available_ingredients()
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

    def test_available_ingredients_contains_sauce_type(self, db):
        ingredients = db.available_ingredients()
        types = {ing.get_type() for ing in ingredients}
        assert INGREDIENT_TYPE_SAUCE in types

    def test_available_ingredients_contains_filling_type(self, db):
        ingredients = db.available_ingredients()
        types = {ing.get_type() for ing in ingredients}
        assert INGREDIENT_TYPE_FILLING in types
