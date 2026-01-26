import pytest
from praktikum.ingredient_types import *


class TestDatabase:
    @pytest.mark.parametrize("expected_bun, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_available_buns(self, db, expected_bun, expected_price):
        buns_db = db.available_buns()
        bun = next(bun for bun in buns_db if bun.get_name() == expected_bun)
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize("expected_ingredient, expected_type, expected_price", [
        ("hot sauce", INGREDIENT_TYPE_SAUCE, 100),
        ("sour cream", INGREDIENT_TYPE_SAUCE, 200),
        ("chili sauce", INGREDIENT_TYPE_SAUCE, 300)
    ])
    def test_available_ingredients(self, db, expected_ingredient, expected_type, expected_price):
        ingredients = db.available_ingredients()
        ingredient = next(ingredient for ingredient in ingredients if ingredient.get_name() == expected_ingredient)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_price() == expected_price