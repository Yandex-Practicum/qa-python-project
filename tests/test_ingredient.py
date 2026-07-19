import pytest

from ingredient import Ingredient
from data import DataIngredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', DataIngredient.data_create_ingredient)
    def test_create_ingredient_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.name == name
        assert ingredient.price == price
        assert ingredient.type == ingredient_type

    def test_get_name_return_name(self):
        ingredient = Ingredient('SAUCE', "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    def test_get_price_return_price(self):
        ingredient = Ingredient('SAUCE', "hot sauce", 100)
        assert ingredient.get_price() == 100

    def test_get_type_return_type(self):
        ingredient = Ingredient('SAUCE', "hot sauce", 100)
        assert ingredient.get_type() == 'SAUCE'

