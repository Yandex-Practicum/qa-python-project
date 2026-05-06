from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING 
from praktikum.ingredient import Ingredient
from data.ingredient_data import INGREDIENT_PRICE_SAUCE, INGREDIENT_NAME_SAUCE, INGREDIENT_NAME_FILLING, INGREDIENT_PRICE_FILLING
import pytest

class TestIngredient: 
    def test_get_price_returns_correct_price(self, ingredient):
        assert ingredient.get_price() == INGREDIENT_PRICE_SAUCE

    def test_get_name_returns_correct_name(self, ingredient):
        assert ingredient.get_name() == INGREDIENT_NAME_SAUCE

    @pytest.mark.parametrize("ingredient_obj,expected_type", [
        (Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME_SAUCE, INGREDIENT_PRICE_SAUCE), INGREDIENT_TYPE_SAUCE),
        (Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_FILLING, INGREDIENT_PRICE_FILLING), INGREDIENT_TYPE_FILLING) 
    ])
    def test_get_type_returns_correct_type(self, ingredient_obj, expected_type):
        assert ingredient_obj.get_type() == expected_type           
 