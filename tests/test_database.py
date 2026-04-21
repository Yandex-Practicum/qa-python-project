import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    @pytest.mark.parametrize("index,expected_name,expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_bun_at_index_has_correct_name_and_price(self, index, expected_name, expected_price):
        db = Database()
        bun = db.available_buns()[index]
        assert bun.get_name() == expected_name and bun.get_price() == expected_price
    
    @pytest.mark.parametrize("index,expected_type", [
        (0, INGREDIENT_TYPE_SAUCE),
        (1, INGREDIENT_TYPE_SAUCE),
        (2, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING),
        (4, INGREDIENT_TYPE_FILLING),
        (5, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_at_index_has_correct_type(self, index, expected_type):
        db = Database()
        ingredient = db.available_ingredients()[index]
        assert ingredient.get_type() == expected_type