import pytest
from tests.data import *


class TestDatabase:


    @pytest.mark.parametrize('bun_index, bun_name, bun_price', BUNS)
    def test_available_buns(self, database, bun_index, bun_name, bun_price):
        assert database.available_buns()[bun_index].get_name() == bun_name
        assert database.available_buns()[bun_index].get_price() == bun_price

    @pytest.mark.parametrize('ing_index, ing_type, ing_name, ing_price', INGREDIENTS)
    def test_available_ingredients(self, database, ing_index, ing_type, ing_name, ing_price):
        assert database.available_ingredients()[ing_index].get_type() == ing_type
        assert database.available_ingredients()[ing_index].get_name() == ing_name
        assert database.available_ingredients()[ing_index].get_price() == ing_price