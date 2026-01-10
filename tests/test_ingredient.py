import allure
import pytest

from praktikum.ingredient import Ingredient
from data import Data
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @allure.title('Проверяем создание ингредиента')
    @allure.description('Проверяем, что возможно создать ингредиент типом, именем и ценой')
    def test_create_ingredient_actual_type_name_and_price_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert ingredient.type == Data.INGREDIENT_TYPE
        assert ingredient.name == Data.INGREDIENT_NAME
        assert ingredient.price == Data.INGREDIENT_PRICE

    @allure.title('Проверяем получение имени ингредиента')
    @allure.description('Проверяем, что возможно получить имя ингредиента методом get_name')
    def test_get_name_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert ingredient.get_name() == Data.INGREDIENT_NAME

    @allure.title('Проверяем получение цены ингредиента')
    @allure.description('Проверяем, что возможно получить цену ингредиента методом get_price')
    def test_get_price_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert ingredient.get_price() == Data.INGREDIENT_PRICE

    @allure.title('Проверяем получение типа ингредиента')
    @allure.description('Проверяем, что возможно получить тип ингредиента методом get_type')
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_success(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert ingredient.get_type() == ingredient_type
