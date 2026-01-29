import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestIngredient:
        
    def test_correct_name_of_ingredient(self, ingredient):
        assert ingredient.get_name() == 'Соус традиционный галактический'

    def test_correct_price_of_ingredient(self, ingredient):
        assert ingredient.get_price() == 15

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300, 'FILLING']
        ]
    )
    def test_correct_type_of_ingredient(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient
    
