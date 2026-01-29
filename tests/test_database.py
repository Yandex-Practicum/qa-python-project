import allure
import pytest
from data import TestDataBase

class TestDataBas:
    @allure.title('Проверка метода available_buns')
    @allure.description('Получаем список булок из БД')
    @pytest.mark.parametrize('id, name, price', TestDataBase.bun)
    def test_available_bun(self, id, name, price, data_base):
        data = data_base.available_buns()
        assert data[id].get_name() == name and data[id].get_price() == price

    @allure.title('Проверка метода available_buns')
    @allure.description('Получаем список ингредиентов из БД')
    @pytest.mark.parametrize('id, type, name, price', TestDataBase.ingredients)
    def test_available_bun(self, id, type, name, price, data_base):
        data = data_base.available_ingredients()
        assert data[id].get_name() == name and data[id].get_type() == type and data[id].get_price() == price