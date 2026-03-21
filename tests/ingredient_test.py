import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 250.5),
        ("CUSTOM_TYPE", "Custom Item", 0), 
        (INGREDIENT_TYPE_SAUCE, "Mayo", 99.99)
    ])
    def test_ingredient_creation_and_getters(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)

        assert ingredient.type == ing_type
        assert ingredient.name == name
        assert ingredient.price == price

        assert ingredient.get_type() == ing_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_modification(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Old Sauce", 100)
        ingredient.type = INGREDIENT_TYPE_FILLING
        ingredient.name = "New Filling"
        ingredient.price = 500
        
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
        assert ingredient.get_name() == "New Filling"
        assert ingredient.get_price() == 500