import pytest
from praktikum.ingredient import Ingredient
from data import TestData

class TestIngredient:
    # Тестирование типа ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    # Тестирование цены ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price


    # Тестирование имени ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name


