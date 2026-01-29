import allure
import pytest

import data
from praktikum.ingredient import Ingredient


class TestIngredient:

    @allure.title('проверка инициализации ингредиента для бургера')
    @pytest.mark.parametrize('type_ing,name,price', data.ingredient_data)
    def test_ingredient_creation(self, type_ing, name, price):
        ingredient = Ingredient(type_ing, name, price)
        assert ingredient.type == type_ing
        assert ingredient.name == name
        assert ingredient.price == price

    @allure.title('Проверка получения цены ингредиента')
    @pytest.mark.parametrize('type_ing,name,price', data.ingredient_data)
    def test_get_price_ingredient(self, type_ing, name, price):
        ingredient = Ingredient(type_ing, name, price)
        assert ingredient.get_price() == price

    @allure.title('Проверка получения имени ингредиента')
    @pytest.mark.parametrize('type_ing,name,price', data.ingredient_data)
    def test_get_name(self, type_ing, name, price):
        ingredient = Ingredient(type_ing, name, price)
        assert ingredient.get_name() == name

    @allure.title('Проверка получчения типа ингредиента')
    @pytest.mark.parametrize('type_ing,name,price', data.ingredient_data)
    def test_get_type(self, type_ing, name, price):
        ingredient = Ingredient(type_ing, name, price)
        assert ingredient.get_type() == type_ing
