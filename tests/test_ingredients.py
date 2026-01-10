import pytest
import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from helpers import Data


class TestIngredient:
    @allure.title('Проверяем получение цены ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_SAUCE,
                                                               Data.CHILI_SAUCE,
                                                               Data.CHILI_SAUCE_PRICE]])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @allure.title('Проверяем получение названия ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_SAUCE,
                                                               Data.HOT_SAUCE,
                                                               Data.HOT_SAUCE_PRICE]])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @allure.title('Проверяем получение типа ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_FILLING,
                                                               Data.SOUR_CREAM,
                                                               Data.SOUR_CREAM_PRICE]])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
