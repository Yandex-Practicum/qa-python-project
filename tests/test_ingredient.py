import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 20, INGREDIENT_TYPE_SAUCE, "hot sauce", 20),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_SAUCE, "ketchup", 15, INGREDIENT_TYPE_SAUCE, "ketchup", 15),
            (INGREDIENT_TYPE_FILLING, "cheese", 50, INGREDIENT_TYPE_FILLING, "cheese", 50),
        ]
    )
    def test_ingredient_initialization(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price
