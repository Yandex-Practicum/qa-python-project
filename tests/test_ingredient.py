import pytest
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_init(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient.get_name() == "Hot Sauce"
        assert ingredient.get_price() == 100.0

    @pytest.mark.parametrize("ingredient_type,expected_type", [
        (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING),
    ])
    def test_get_type(self, ingredient_type, expected_type):
        ingredient = Ingredient(ingredient_type, "Hot Sauce", 100.0)
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize("name,expected_name", [
        ("Hot Sauce", "Hot Sauce"),
        ("Sour Cream", "Sour Cream"),
    ])
    def test_get_name(self, name, expected_name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100.0)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize("price,expected_price", [
        (100.0, 100.0),
        (200.0, 200.0),
        (0.0, 0.0),
    ])
    def test_get_price(self, price, expected_price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", price)
        assert ingredient.get_price() == expected_price

    def test_none_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, None, 100.0)
        assert ingredient.get_name() is None

    def test_none_type(self):
        ingredient = Ingredient(None, "Unknown Ingredient", 100.0)
        assert ingredient.get_type() is None
