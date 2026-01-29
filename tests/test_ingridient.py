import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from data import TestData


class TestIngredient:

    @pytest.mark.parametrize('ingredient_name', ['бекон', 'cheese', '342', 'Лук с кожурками'])
    def test_get_ingridient_name(self, ingredient_name):
        #проверка что возвращается правильное имя ингридиента
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, ingredient_name, TestData.ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('ingredient_price', [1, 2.49, 125, 3999])
    def test_get_ingridient_price(self, ingredient_price):
        #проверка что возвращается правильная стоимость ингридиента
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, TestData.ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_get_ingridient_type(self, ingredient_type):
        #проверка что возвращается правильный тип ингридиента
        ingredient = Ingredient(ingredient_type, TestData.ingredient_name, TestData.ingredient_price)
        assert ingredient.get_type() == ingredient_type
