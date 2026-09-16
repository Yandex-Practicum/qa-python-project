import pytest
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_init(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient.get_name() == "Hot Sauce"
        assert ingredient.get_price() == 100.0

    @pytest.mark.parametrize("ingredient_type,name,price,expected_type,expected_name,expected_price", [
        (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100.0, INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100.0),
        (INGREDIENT_TYPE_SAUCE, "Sour Cream", 200.0, INGREDIENT_TYPE_SAUCE, "Sour Cream", 200.0),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 150.0, INGREDIENT_TYPE_FILLING, "Cutlet", 150.0),
        (INGREDIENT_TYPE_FILLING, "Dinosaur", 250.0, INGREDIENT_TYPE_FILLING, "Dinosaur", 250.0),
        (INGREDIENT_TYPE_SAUCE, "", 0.0, INGREDIENT_TYPE_SAUCE, "", 0.0),
    ])
    def test_getters(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price

    def test_negative_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Bad Sauce", -50.0)
        assert ingredient.get_price() == -50.0

    def test_none_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, None, 100.0)
        assert ingredient.get_name() is None

    def test_none_type(self):
        ingredient = Ingredient(None, "Unknown Ingredient", 100.0)
        assert ingredient.get_type() is None
