from data import TestDataBase
from conftest import db
import pytest
import allure


class TestDatabase:
    @allure.title('Проверка метода available_buns, который показывает доступные булочки из базы данных')
    @allure.description('Выполняем три теста - проверяем имя и стоимость каждой булки')
    @pytest.mark.parametrize('bun_index, expected_bun_name, expected_bun_price', TestDataBase.test_data_base_buns)
    def test_available_buns_db_success(self, db, bun_index, expected_bun_name, expected_bun_price):
        data_buns = db.available_buns()
        assert data_buns[bun_index].get_name() == expected_bun_name and data_buns[bun_index].get_price() == expected_bun_price

    @allure.title('Проверка работы метода available_ingredients, который показывает доступные ингредиенты из базы данных')
    @allure.description('Выполняем шесть тестов - проверяем имя, тип и стоимость каждого ингредиента')
    @pytest.mark.parametrize('ingredient_index, type_ingredient, expected_name, expected_price', TestDataBase.test_data_base_ingredients)
    def test_available_ingredients_db_success(self, db, ingredient_index, type_ingredient, expected_name, expected_price):
        ingredients_data = db.available_ingredients()
        assert (ingredients_data[ingredient_index].get_name() == expected_name and
                ingredients_data[ingredient_index].get_type() == type_ingredient and
                ingredients_data[ingredient_index].get_price() == expected_price)