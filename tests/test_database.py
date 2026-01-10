import allure
import pytest
from conftest import data_base
from data import DataBase

class TestDataBase:

    @allure.title('Проверка метода get_type')
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', DataBase.database_buns)
    def test_available_buns_works_correctly(self, data_base, index_bun, bun_name, bun_price):
        data_buns = data_base.available_buns()
        assert data_buns[index_bun].get_name() == bun_name
        assert data_buns[index_bun].get_price() == bun_price

    @allure.title('Проверка метода available_ingredients')
    @pytest.mark.parametrize('index_ingredient, type_ingredient, name_ingredient, price_ingredient', DataBase.database_ingredients)
    def test_available_ingredients_works_correctly(self, data_base, type_ingredient, index_ingredient, name_ingredient, price_ingredient):
        data_ingrediets = data_base.available_ingredients()
        assert data_ingrediets[index_ingredient].get_name() == name_ingredient
        assert data_ingrediets[index_ingredient].get_type() == type_ingredient
        assert data_ingrediets[index_ingredient].get_price() == price_ingredient