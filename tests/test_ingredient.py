import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', [(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100), (INGREDIENT_TYPE_FILLING, 'cutlet', 100), (INGREDIENT_TYPE_SAUCE, 'chili sauce', 300)])
    def test_ingredient_creation_correct_data_return_correct_type_name_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name        
        assert ingredient.get_price() == price