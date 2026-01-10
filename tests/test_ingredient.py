import allure
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock

class TestIngredient:

    @allure.title('Получение цены')
    @pytest.mark.parametrize('ingredient, name, price', [
    (INGREDIENT_TYPE_FILLING, 'Cheese', 20.99),
    (INGREDIENT_TYPE_SAUCE, 'Barbecue', 5.99)
])
    def test_get_price(self, ingredient, name, price):
        ingr = Ingredient(ingredient, name, price)
        assert ingr.get_price() == price

    @allure.title('Проеверка названия')
    @pytest.mark.parametrize('ingredient, name, price', [
    (INGREDIENT_TYPE_FILLING, 'Cheese', 20.99),
    (INGREDIENT_TYPE_SAUCE, 'Barbecue', 5.99)
])
    def test_get_name(self, ingredient, name, price):
        ingr = Ingredient(ingredient, name, price)
        assert ingr.get_name() == name

    @allure.title('Проеверка типа ингредиента')
    @pytest.mark.parametrize('ingredient, name, price', [
    (INGREDIENT_TYPE_FILLING, 'Cheese', 20.99),
    (INGREDIENT_TYPE_SAUCE, 'Barbecue', 5.99)
])
    def test_get_type(self, ingredient, name, price):
        ingr = Ingredient(ingredient, name, price)
        assert ingr.get_type() == ingredient
