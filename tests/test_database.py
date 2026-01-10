import pytest
from data import DatabaseInfo
from conftest import init_database

class TestDatabase:
    @pytest.mark.parametrize('bun_index, bun_name, bun_price', DatabaseInfo().buns_database)
    def test_available_buns(self, init_database, bun_index, bun_name, bun_price):
        buns_info = init_database.available_buns()
        assert buns_info[bun_index].get_name() == bun_name and buns_info[bun_index].get_price() == bun_price

    @pytest.mark.parametrize('ingredient_index, ingredient_type, ingredient_name, ingredient_price',
                             DatabaseInfo().ingredients_database)
    def test_available_ingredients(self, init_database, ingredient_index, ingredient_type, ingredient_name, ingredient_price):
        ingredients_info = init_database.available_ingredients()
        assert (ingredients_info[ingredient_index].get_name() == ingredient_name and
                ingredients_info[ingredient_index].get_price() == ingredient_price)
