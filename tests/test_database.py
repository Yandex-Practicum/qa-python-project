import pytest


class TestDatabase:

    @pytest.mark.parametrize('list_key, name, price', [[0, 'black bun', 100], [1, 'white bun', 200]])
    def test_available_buns(self, new_database, list_key, name, price):
        assert new_database.available_buns()[list_key].get_name() == name
        assert new_database.available_buns()[list_key].get_price() == price

    @pytest.mark.parametrize('list_key, type, name, price', [[0, 'SAUCE', 'hot sauce', 100], [3, 'FILLING', 'cutlet', 100]])
    def test_available_ingredients(self, new_database, list_key, type, name, price):
        assert new_database.available_ingredients()[list_key].get_type() == type
        assert new_database.available_ingredients()[list_key].get_name() == name
        assert new_database.available_ingredients()[list_key].get_price() == price
