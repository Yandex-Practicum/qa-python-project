from data import DataIngredient, DataBun
from praktikum.database import Database

import pytest

class TestDataBase:
        @pytest.mark.parametrize("expected_buns, expected_price", DataBun.DATA_BUNS_DATABASE)
        def test_available_buns(self, expected_buns, expected_price):
            database = Database()
            buns = database.available_buns()
            assert expected_buns, expected_price in buns

        @pytest.mark.parametrize("expected_type,expected_ingredient, expected_price", DataIngredient.DATA_SAUCE_DATABASE)
        def test_available_sauce_ingredients(self, expected_type,expected_ingredient, expected_price):
            database = Database()
            ingredients = database.available_ingredients()
            sauce = expected_ingredient, expected_price
            assert expected_type, sauce in ingredients

        @pytest.mark.parametrize("expected_type,expected_ingredient, expected_price", DataIngredient.DATA_FILLING_DATABASE)
        def test_available_sauce_ingredients(self, expected_type, expected_ingredient, expected_price):
            database = Database()
            ingredients = database.available_ingredients()
            sauce = expected_ingredient, expected_price
            assert expected_type, sauce in ingredients