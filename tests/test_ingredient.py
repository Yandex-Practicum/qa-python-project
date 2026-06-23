
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import data

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredient_return_correct_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type,name, price)
        
        assert ingredient.get_type() == ingredient_type

    
    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredient_return_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type,name, price)
        
        assert ingredient.get_name() == name

    
    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredient_return_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type,name, price)
        
        assert ingredient.get_price() == price
        