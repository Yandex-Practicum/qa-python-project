import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    """Tests for the Ingredient class."""

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Ketchup", 50),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 80),
    ])
    def test_getters_return_correct_values(self, ing_type, name, price):
        """
        Ingredient.get_type, get_name, and get_price should return the values
        provided to the constructor.
        """
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type, "get_type() should return the ingredient type"
        assert ingredient.get_name() == name, "get_name() should return the ingredient name"
        assert ingredient.get_price() == price, "get_price() should return the ingredient price"
