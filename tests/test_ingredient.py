import pytest
import data as D
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price', D.INGREDIENT_PARAMS)
    def test_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name 
        assert ingredient.price == price

    def test_get_ingredient_type(self, filling):
        assert filling.get_type() == D.INGREDIENT_TYPE_FILLING

    def test_get_ingredient_name(self, filling):
        assert filling.get_name() == D.INGREDIENT_FILLING_NAME

    def test_get_ingredient_price(self, filling):
        assert filling.get_price() == D.INGREDIENT_FILLING_1_PRICE