import allure
import pytest

from praktikum.ingredient import Ingredient
from data import TestData


@pytest.mark.parametrize("ingredient_type, name, price", TestData.ingredients)
class TestIngredient:

    @allure.title("Проверка получения цены ингредиента")
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @allure.title("Проверка получения названия ингредиента")
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @allure.title("Проверка получения типа ингредиента(начинка или соус)")
    def test_get_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
