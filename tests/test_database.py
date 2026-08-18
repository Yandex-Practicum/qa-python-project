import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    # Тесты для available_buns()
    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_contains_three_items(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_buns_returns_bun_objects(self):
        db = Database()
        buns = db.available_buns()
        for bun in buns:
            assert isinstance(bun, Bun)

    @pytest.mark.parametrize("bun_name", [
        "black bun",
        "white bun",
        "red bun"
    ])
    def test_available_buns_contains_bun(self, bun_name):
        db = Database()
        buns = db.available_buns()
        names = [bun.get_name() for bun in buns]
        assert bun_name in names

    # Тесты для available_ingredients()
    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_contains_six_items(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_returns_ingredient_objects(self):
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

    @pytest.mark.parametrize("ingredient_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING
    ])
    def test_available_ingredients_contains_type(self, ingredient_type):
        db = Database()
        ingredients = db.available_ingredients()
        types = [ingredient.get_type() for ingredient in ingredients]
        assert ingredient_type in types

    @pytest.mark.parametrize("ingredient_name", [
        "hot sauce",
        "sour cream",
        "chili sauce",
        "cutlet",
        "dinosaur",
        "sausage"
    ])
    def test_available_ingredients_contains_ingredient(self, ingredient_name):
        db = Database()
        ingredients = db.available_ingredients()
        names = [ingredient.get_name() for ingredient in ingredients]
        assert ingredient_name in names
        