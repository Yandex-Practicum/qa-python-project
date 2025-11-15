import pytest
from praktikum.database import Database


class TestDatabase:

  
    @pytest.mark.parametrize('index, expected_name', [(0, "black bun"),(1, "white bun"),(2, "red bun")])
    def test_available_buns_return_correct_names(self, index, expected_name):
        database = Database()
        buns = database.available_buns()
        assert buns[index].name == expected_name

    @pytest.mark.parametrize('index, expected_price', [(0, 100),(1, 200),(2, 300)])
    def test_available_buns_return_correct_price(self, index, expected_price):
        database = Database()
        buns = database.available_buns()
        assert buns[index].price == expected_price

    @pytest.mark.parametrize('index, expected_name', [(0, "hot sauce"), (1, "sour cream"), (2, "chili sauce"), (3, "cutlet"), (4, "dinosaur"), (5, "sausage")])
    def test_available_ingredient_return_correct_names(self, index, expected_name):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].name == expected_name

    @pytest.mark.parametrize('index, expected_type', [(0, "SAUCE"), (1, "SAUCE"), (2, "SAUCE"), (3, "FILLING"), (4, "FILLING"), (5, "FILLING")])
    def test_available_ingredients_return_correct_types(self, index, expected_type):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].get_type() == expected_type

    @pytest.mark.parametrize('index, expected_price', [(0, 100), (1, 200), (2, 300), (3, 100), (4, 200), (5, 300)])
    def test_available_ingredients_return_correct_prices(self, index, expected_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].get_price() == expected_price


 