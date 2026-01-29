import pytest
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import DataAvailable

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_buns_names(self):
        db = Database()
        buns = db.available_buns()
        actual_names = [bun.name for bun in buns]
        assert actual_names == DataAvailable.AVAILABLE_BUNS_NAMES

    def test_available_buns_prices(self):
        db = Database()
        buns = db.available_buns()
        actual_prices = [bun.price for bun in buns]
        assert actual_prices == DataAvailable.AVAILABLE_BUNS_PRICES

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_names(self):
        db = Database()
        ingredients = db.available_ingredients()
        actual_names = [ingredient.name for ingredient in ingredients]
        assert actual_names == DataAvailable.AVAILABLE_INGREDIENTS_NAMES

    def test_available_ingredients_prices(self):
        db = Database()
        ingredients = db.available_ingredients()
        actual_prices = [ingredient.price for ingredient in ingredients]
        assert actual_prices == DataAvailable.AVAILABLE_INGREDIENTS_PRICES

    def test_available_ingredients_types(self):
        db = Database()
        types = db.available_ingredients()
        expected_types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING]
        actual_types = [type.type for type in types]
        assert actual_types == expected_types
