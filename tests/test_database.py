import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database

class TestDatabase:

    def test_available_buns_success(self, mock_bun):
        database = Database()
        assert database.available_buns()[0].name == "black bun"
        assert database.available_buns()[0].price == 100

    def test_available_ingredients_success(self, mock_ingredient):
        database = Database()
        assert database.available_ingredients()[0].type == 'SAUCE'
        assert database.available_ingredients()[0].name == 'hot sauce'
        assert database.available_ingredients()[0].price == 100