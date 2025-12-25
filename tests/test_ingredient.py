import pytest

from praktikum.ingredient import Ingredient
from constants import Constants

class TestIngredient:
    # Тестируем метод _init_ и все его значения
    @pytest.mark.parametrize("type, name, price",
        [
            [Constants.INGREDIENTS_TYPE[0], Constants.INGREDIENT_NAME1, Constants.INGREDIENT_PRICE1],
            [Constants.INGREDIENTS_TYPE[1], Constants.INGREDIENT_NAME1, Constants.INGREDIENT_PRICE1]
         ]
    )
    def test_init_type_assigned_type(self,type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.type in Constants.INGREDIENTS_TYPE

    def test_init_name_assigned_name(self):
        ingredient = Ingredient(Constants.INGREDIENTS_TYPE[0], Constants.INGREDIENT_NAME1, Constants.INGREDIENT_PRICE1)
        assert ingredient.name == Constants.INGREDIENT_NAME1

    def test_init_price_assigned_price(self):
        ingredient = Ingredient(Constants.INGREDIENTS_TYPE[0], Constants.INGREDIENT_NAME1, Constants.INGREDIENT_PRICE1)
        assert ingredient.price == Constants.INGREDIENT_PRICE1

    # Тестируем методы

    def test_get_ingredient_type_got_type(self):
        ingredient = Ingredient(Constants.INGREDIENTS_TYPE[0], Constants.INGREDIENT_NAME1, Constants.INGREDIENT_PRICE1)
        assert ingredient.get_type() == Constants.INGREDIENTS_TYPE[0]

    def test_get_ingredient_name_got_name(self):
        ingredient = Ingredient(Constants.INGREDIENTS_TYPE[0], Constants.INGREDIENT_NAME1, Constants.INGREDIENT_PRICE1)
        assert ingredient.get_name() == Constants.INGREDIENT_NAME1

    def test_get_ingredient_price_got_price(self):
        ingredient = Ingredient(Constants.INGREDIENTS_TYPE[0], Constants.INGREDIENT_NAME1, Constants.INGREDIENT_PRICE1)
        assert ingredient.get_price() == Constants.INGREDIENT_PRICE1