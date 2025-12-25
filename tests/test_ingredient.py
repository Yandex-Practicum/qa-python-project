from praktikum.ingredient import Ingredient
from data import SAUCE_NAME,SAUCE_PRICE,FILLING_NAME,FILLING_PRICE
import pytest


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price",
                             [
                                 ('Соус', SAUCE_NAME, SAUCE_PRICE),
                                 ('Начинка', FILLING_NAME, FILLING_PRICE)
                             ]
                             )
    def test_get_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)

        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price",
                             [
                                 ('Соус', SAUCE_NAME, SAUCE_PRICE),
                                 ('Начинка', FILLING_NAME, FILLING_PRICE)
                             ]
                             )
    def test_get_name(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)

        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price",
                             [
                                 ('Соус', SAUCE_NAME, SAUCE_PRICE),
                                 ('Начинка', FILLING_NAME, FILLING_PRICE)
                             ]
                             )
    def test_get_type(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)

        assert ingredient.get_type() == ingredient_type



