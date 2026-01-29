import pytest

from data.database_data import DatabaseData
from praktikum.database import Database


class TestDatabase:

    @pytest.mark.parametrize('param', DatabaseData.param_bun)
    def test_available_buns(self, param):
        name, cod, price = param
        bun_list = Database()
        bun_list.available_buns()
        assert bun_list.buns[cod].get_name() == name and bun_list.buns[cod].get_price() == price

    @pytest.mark.parametrize('param', DatabaseData.param_ingr)
    def test_available_ingredients(self, param):
        name, cod, price = param
        bun_list = Database()
        bun_list.available_buns()
        assert bun_list.ingredients[cod].get_name() == name and bun_list.ingredients[cod].get_price() == price

