import pytest
import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.epic("Stellar Burgers")
@allure.feature("Юнит-тесты компонентов: Ингредиенты")
class TestIngredient:
    @allure.title("Проверка получения типа ингредиента")
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_specified_type_returns_same_type(self, ingredient_type):
        with allure.step(f"Инициализировать ингредиент с типом: {ingredient_type}"):
            ingredient = Ingredient(ingredient_type, 'Тестовый ингредиент', 100.0)
        with allure.step("Вызвать метод get_type() и проверить возвращаемое значение"):
            assert ingredient.get_type() == ingredient_type
    
    @allure.title("Проверка получения названия ингридиента")
    @pytest.mark.parametrize('ingredient_name', ['Соус традиционный галактический',
                                               'Соус с шипами Антарианского плоскоходца',
                                               ''])
    def test_get_name_various_strings_returns_same_string(self, ingredient_name):
        with allure.step(f"Инициализировать ингредиент с названием: '{ingredient_name}'"):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, ingredient_name, 150.0)
        with allure.step('Вызвать метод get_name() и проверить возвращаемое значение'):
            assert ingredient.get_name() == ingredient_name

    @allure.title("Проверка получения цены ингридиента")
    @pytest.mark.parametrize('ingredient_price', [0.0, 
        415.5, 
        1000.0])
    def test_get_price_various_amounts_returns_same_amount(self, ingredient_price):
        with allure.step(f"Инициализировать ингредиент с ценой: {ingredient_price}"):
            ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Динамический ингредиент', ingredient_price)
        with allure.step("Вызвать метод get_price() и проверить возвращаемое значение"):
            assert ingredient.get_price() == ingredient_price
    

    
