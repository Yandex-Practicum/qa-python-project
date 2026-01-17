from praktikum.ingredient import Ingredient
from data import DataTestIngredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', DataTestIngredient.ingredients_data)
    def test_get_type_create_new_ingredient_check_type(self, ingredient_type, name, price):
        new_ingredient = Ingredient(ingredient_type, name, price)
        assert new_ingredient.get_type() == ingredient_type

    def test_get_name_create_new_ingredient_check_name(self):
        new_ingredient = Ingredient(*DataTestIngredient.ingredient_data_1)
        assert new_ingredient.get_name() == DataTestIngredient.ingredient_data_1[1]

    def test_get_price_create_new_ingredient_check_price(self):
        new_ingredient = Ingredient(*DataTestIngredient.ingredient_data_1)
        assert new_ingredient.get_price() == DataTestIngredient.ingredient_data_1[2]