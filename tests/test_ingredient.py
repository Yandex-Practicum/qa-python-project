import pytest
import allure

from praktikum import Ingredient, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from helpers.helpers import *


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    @allure.title(f'Проверка получения цены ингредиента')
    def test_get_price(self, ingredient_type):
        ingredient_type = ingredient_type
        name = generate_random_string(10)
        price = float(random.randint(1, 1000))
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    @allure.title('Проверка получения названия ингредиента')
    def test_get_name(self, ingredient_type):
        ingredient_type = ingredient_type
        name = generate_random_string(10)
        price = float(random.randint(1, 1000))
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    @allure.title('Проверка получения типа ингредиента')
    def test_get_type(self, ingredient_type):
        ingredient_type = ingredient_type
        name = generate_random_string(10)
        price = float(random.randint(1, 1000))
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

