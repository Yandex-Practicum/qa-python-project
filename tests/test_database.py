import pytest

from data import Data
from praktikum.database import Database


class TestDataBase:

    @pytest.mark.parametrize('data', Data.data_buns)
    def test_available_buns(self, data):
        data_base = Database()
        assert data_base.available_buns()[data[1]].name == data[0] and data_base.available_buns()[data[1]].price == data[2]


    @pytest.mark.parametrize('data', Data.ingridietns)
    def test_available_ingredients(self, data):
        data_base = Database()
        assert data_base.available_ingredients()[data[1]].name == data[0] and data_base.available_ingredients()[data[1]].price == data[2]
