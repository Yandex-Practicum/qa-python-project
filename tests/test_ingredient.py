import pytest
from praktikum.ingredient import Ingredient
from data import TestData

class TestIngredient:
    # тестирование метода получения цены ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # тестирование метода получения названия ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # тестирование метода получения типа ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type