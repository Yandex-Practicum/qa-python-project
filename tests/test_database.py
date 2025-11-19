import pytest
from data import expected_buns, expected_ingredients
from praktikum.database import Database

class TestDatabase:

    def test_available_buns_returns_list(self):
        database = Database()
        assert isinstance(database.available_buns(), list)

    def test_available_ingredients_returns_list(self):
        database = Database()
        assert isinstance(database.available_ingredients(), list)

    @pytest.mark.parametrize("index, bun_name, bun_price", expected_buns)
    def test_available_buns_return_available_bun(self, index, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()
        assert buns[index].name == bun_name

    @pytest.mark.parametrize("index, bun_name, bun_price", expected_buns)
    def test_available_buns_return_available_price(self, index, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()
        assert buns[index].price == bun_price

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_available_ingredients_return_available_ingredients_type(self, index, ingredient_type, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].type == ingredient_type

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_available_ingredients_return_available_ingredients_name(self, index, ingredient_type, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].name == ingredient_name

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_available_ingredients_return_available_ingredients_price(self, index, ingredient_type, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].price == ingredient_price
