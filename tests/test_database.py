import pytest
from conftest import database
from data import TestDataIngredients
import allure


@allure.suite('Тестирование класса - Database')
class TestDataBase:

    @allure.title('Проверка получения списка доступных булочек и их стоимости из БД - available_buns')
    @pytest.mark.parametrize('bun_item, bun_name, bun_price', TestDataIngredients.data_buns)
    def test_available_buns_is_success(self, bun_item, bun_name, bun_price, database):
        buns_list = database.available_buns()
        assert buns_list[bun_item].get_name() == bun_name and buns_list[bun_item].get_price() == bun_price

    @allure.title('Проверка получения списка доступных ингредиентов,их названия,типа и стоимости-available_ingredients')
    @pytest.mark.parametrize('ingredient_item, '
                             'ingredient_name, '
                             'ingredient_type, '
                             'ingredient_price',
                             TestDataIngredients.data_ingredients)
    def test_available_ingredients_is_success(self, ingredient_item,
                                              ingredient_type,
                                              ingredient_name,
                                              ingredient_price,
                                              database):
        ingredient_list = database.available_ingredients()
        assert (ingredient_list[ingredient_item].get_name() == ingredient_type and
        ingredient_list[ingredient_item].get_type() == ingredient_name and
        ingredient_list[ingredient_item].get_price() == ingredient_price)