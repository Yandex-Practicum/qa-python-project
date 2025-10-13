import pytest
import allure

from conftest import create_ingredient
from data import Data

@allure.suite('Тесты класса "ingredient"')
class TestIngredient:

    @allure.title('Проверка типа данных и корректности цены ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', Data.list_ingredient)
    def test_get_price_return_correct_price(self, ingredient_type, name, price, create_ingredient):
        assert type(create_ingredient.get_price()) == float and create_ingredient.get_price() == price

    @allure.title('Проверка типа данных и корректности имени ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', Data.list_ingredient)
    def test_get_name_return_correct_name(self, ingredient_type, name, price,create_ingredient):
        assert type(create_ingredient.get_name()) == str and create_ingredient.get_name() == name

    @allure.title('Проверка типа данных и корректности типа ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', Data.list_ingredient)
    def test_get_type_return_correct_type(self, ingredient_type, name, price, create_ingredient):
        assert type(create_ingredient.get_type()) == str and create_ingredient.get_type() == ingredient_type

    @allure.title('Проверка создания ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', Data.list_ingredient)
    def test_init_correct_ingredient(self, ingredient_type, name, price, create_ingredient):
        assert create_ingredient.name == name and create_ingredient.price == price and create_ingredient.type == ingredient_type