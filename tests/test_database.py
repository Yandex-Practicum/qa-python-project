import pytest
from data import TestData
from helper import *


class TestDatabase:

    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestData.test_data_buns)
    def test_available_buns(self, index_bun,db, bun_name, bun_price):
        bun_data = get_bun_data(db)
        assert bun_data[index_bun][0] == bun_name
        assert bun_data[index_bun][1] == bun_price

    @pytest.mark.parametrize('index, ingredient_type, ingredient_name, ingredient_price',TestData.test_data_ingredients)
    def test_available_ingredients(self, index,db, ingredient_type, ingredient_name, ingredient_price):
        ingredient_data = get_ingredient_data(db)
        assert ingredient_data[index][0] == ingredient_type
        assert ingredient_data[index][1] == ingredient_name
        assert ingredient_data[index][2] == ingredient_price

    def test_get_quantity_available_sauces(self,db):
        ingredient_data = get_ingredient_data(db)
        sauces = filter_by_type(ingredient_data, 'SAUCE')
        assert len(sauces) == 3

    def test_get_quantity_available_fillings(self,db):
        ingredient_data = get_ingredient_data(db)
        fillings = filter_by_type(ingredient_data, 'FILLING')
        assert len(fillings) == 3

    def test_get_ingredients_prices(self,db):
        ingredient_data = get_ingredient_data(db)
        price = get_price_dict(ingredient_data)
        assert price['hot sauce'] == 100
        assert price['sour cream'] == 200
        assert price['chili sauce'] == 300
        assert price['cutlet'] == 100
        assert price['dinosaur'] == 200
        assert price['sausage'] == 300
