import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize(
        "ing_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "sour cream", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 50),
        ]
    )
    def test_ingredient_getters(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        
        assert ingredient.get_type() == ing_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_initialization(self):
        ing_type = INGREDIENT_TYPE_FILLING
        name = "chicken"
        price = 150
        
        ingredient = Ingredient(ing_type, name, price)
        
        assert ingredient.type == ing_type
        assert ingredient.name == name
        assert ingredient.price == price