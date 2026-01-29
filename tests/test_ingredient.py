import pytest
from pages.ingredient import Ingredient
from pages.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_constructor_sets_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_constructor_sets_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 200)
        assert ingredient.get_name() == "Cutlet"

    def test_constructor_sets_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Sausage", 300)
        assert ingredient.get_price() == 300

    def test_get_name_returns_correct_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Sour Cream", 150)
        assert ingredient.get_name() == "Sour Cream"

    def test_get_price_returns_correct_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Fish", 250)
        assert ingredient.get_price() == 250