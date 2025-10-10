import pytest
from data.database_data import params_bun_name, params_bun_price, params_ingredients_type, params_ingredients_name, params_ingredients_price
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_check_bun_list_length(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    def test_check_bun_type_list(self):
        database = Database()
        buns = database.available_buns()
        assert isinstance(buns, list)

    def test_check_bun_object(self):
        database = Database()
        buns = database.available_buns()
        for bun in buns:
            assert isinstance(bun, Bun)

    @pytest.mark.parametrize("index, name", params_bun_name)
    def test_check_bun_name(self, index, name):
        database = Database()
        bun = database.available_buns()[index]
        assert isinstance(bun, Bun) and bun.get_name() == name

    @pytest.mark.parametrize("index, price", params_bun_price)
    def test_check_bun_price(self, index, price):
        database = Database()
        bun = database.available_buns()[index]
        assert isinstance(bun, Bun) and bun.get_price() == price

    def test_check_ingredients_list_length(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_check_ingredients_type(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)

    def test_check_ingredients_object(self):
        database = Database()
        ingredients = database.available_ingredients()
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

    @pytest.mark.parametrize("index, expected_type", params_ingredients_type)
    def test_check_ingredients_type_list(self, index, expected_type):
        database = Database()
        ingredient = database.available_ingredients()[index]
        assert isinstance(ingredient, Ingredient) and ingredient.get_type() == expected_type

    @pytest.mark.parametrize("index, expected_name", params_ingredients_name)
    def test_check_ingredients_name(self, index, expected_name):
        database = Database()
        ingredient = database.available_ingredients()[index]
        assert isinstance(ingredient, Ingredient) and ingredient.get_name() == expected_name

    @pytest.mark.parametrize("index, expected_price", params_ingredients_price)
    def test_check_ingredients_price(self, index, expected_price):
        database = Database()
        ingredient = database.available_ingredients()[index]
        assert isinstance(ingredient, Ingredient) and ingredient.get_price() == expected_price
