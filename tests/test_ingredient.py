import allure
import pytest
from praktikum.ingredient import Ingredient
from data import SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE, FILLING_TYPE, FILLING_NAME, FILLING_PRICE

class TestIngredient:
    @allure.title('Получение типа ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE),
        (FILLING_TYPE, FILLING_NAME, FILLING_PRICE)
    ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @allure.title('Получение названия ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE),
        (FILLING_TYPE, FILLING_NAME, FILLING_PRICE)
    ])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @allure.title('Получение цены ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE),
        (FILLING_TYPE, FILLING_NAME, FILLING_PRICE)
    ])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
