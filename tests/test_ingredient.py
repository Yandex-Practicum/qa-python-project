import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        ("UNKNOWN", "strange", 0),
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self, hot_sauce):
        assert hot_sauce.get_price() == 100

    def test_get_name(self, hot_sauce):
        assert hot_sauce.get_name() == "hot sauce"

    def test_get_type(self, cutlet):
        assert cutlet.get_type() == INGREDIENT_TYPE_FILLING