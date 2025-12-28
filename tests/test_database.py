import pytest
from data import DataBaseBurger
from unittest.mock import Mock
from praktikum.database import Database


class TestDatabase:
    @pytest.mark.parametrize('index, name, price', DataBaseBurger.DATA_LIST_BUNS)
    def test_database_buns(self, index, name, price):
        data_base = Database()
        assert name == data_base.buns[index].get_name()
        assert price == data_base.buns[index].get_price()


    @pytest.mark.parametrize('index, type_ingredient, name, price', DataBaseBurger.DATA_LIST_INGREDIENTS)
    def test_database_ingredients(self, index, type_ingredient, name, price):
        data_base = Database()
        assert type_ingredient == data_base.ingredients[index].get_type()
        assert name == data_base.ingredients[index].get_name()
        assert price == data_base.ingredients[index].get_price()

    def test_available_buns(self):
        mock_buns = Mock()
        data_base = Database()
        data_base.buns = [mock_buns]
        assert mock_buns in data_base.available_buns()

    def test_available_ingredients(self):
        mock_ingredients = Mock()
        data_base = Database()
        data_base.ingredients = [mock_ingredients]
        assert mock_ingredients in data_base.available_ingredients()