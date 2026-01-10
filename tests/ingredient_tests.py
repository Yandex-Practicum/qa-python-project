import pytest

from ingredient import Ingredient
from data import Data

class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price',
                             ((Data.ingr_2[0], Data.ingr_2[1], Data.ingr_2[2]),
                              (Data.ingr_3[0], Data.ingr_3[1], Data.ingr_3[2])))
    def test_ingredients_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type


    @pytest.mark.parametrize('ingredient_type, name, price',
                             ((Data.ingr_2[0], Data.ingr_2[1], Data.ingr_2[2]),
                              (Data.ingr_3[0], Data.ingr_3[1], Data.ingr_3[2])))
    def test_ingredients_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             ((Data.ingr_2[0], Data.ingr_2[1], Data.ingr_2[2]),
                              (Data.ingr_3[0], Data.ingr_3[1], Data.ingr_3[2])))
    def test_ingredients_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
