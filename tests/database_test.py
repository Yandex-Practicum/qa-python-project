import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_initialization_creates_three_buns(self):
        database = Database()
        assert len(database.buns) == 3

    def test_database_initialization_creates_six_ingredients(self):
        database = Database()
        assert len(database.ingredients) == 6

    def test_database_available_buns_returns_three_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    def test_database_first_bun_name_black_bun(self):
        database = Database()
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_database_second_bun_name_white_bun(self):
        database = Database()
        buns = database.available_buns()
        assert buns[1].get_name() == "white bun"

    def test_database_third_bun_name_red_bun(self):
        database = Database()
        buns = database.available_buns()
        assert buns[2].get_name() == "red bun"

    def test_database_available_ingredients_returns_six_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_database_first_bun_price_correct(self):
        database = Database()
        buns = database.available_buns()
        assert buns[0].get_price() == 100

    def test_database_second_bun_price_correct(self):
        database = Database()
        buns = database.available_buns()
        assert buns[1].get_price() == 200

    def test_database_third_bun_price_correct(self):
        database = Database()
        buns = database.available_buns()
        assert buns[2].get_price() == 300

    def test_database_three_sauce_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        sauce_count = 0
        
        for ingredient in ingredients:
            if ingredient.get_type() == INGREDIENT_TYPE_SAUCE:
                sauce_count += 1
        assert sauce_count == 3

    def test_database_three_filling_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        filling_count = 0
        
        for ingredient in ingredients:
            if ingredient.get_type() == INGREDIENT_TYPE_FILLING:
                filling_count += 1
        assert filling_count == 3

    @pytest.mark.parametrize("bun_index, expected_name", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun")
    ])
    def test_database_bun_names_parametrized(self, bun_index, expected_name):
        """Параметризованная проверка названий булочек."""
        database = Database()
        bun = database.available_buns()[bun_index]
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("bun_index, expected_price", [
        (0, 100),
        (1, 200),
        (2, 300)
    ])
    def test_database_bun_prices_parametrized(self, bun_index, expected_price):
        database = Database()
        bun = database.available_buns()[bun_index]
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize("ingredient_index, expected_type", [
        (0, INGREDIENT_TYPE_SAUCE),
        (1, INGREDIENT_TYPE_SAUCE),
        (2, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING),
        (4, INGREDIENT_TYPE_FILLING),
        (5, INGREDIENT_TYPE_FILLING)
    ])
    def test_database_ingredient_types_parametrized(self, ingredient_index, expected_type):
        database = Database()
        ingredient = database.available_ingredients()[ingredient_index]
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize("ingredient_index, expected_name", [
        (0, "hot sauce"),
        (1, "sour cream"),
        (2, "chili sauce"),
        (3, "cutlet"),
        (4, "dinosaur"),
        (5, "sausage")
    ])
    def test_database_ingredient_names_parametrized(self, ingredient_index, expected_name):
        database = Database()
        ingredient = database.available_ingredients()[ingredient_index]
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize("ingredient_index, expected_price", [
        (0, 100),
        (1, 200),
        (2, 300),
        (3, 100),
        (4, 200),
        (5, 300)
    ])
    def test_database_ingredient_prices_parametrized(self, ingredient_index, expected_price):
        database = Database()
        ingredient = database.available_ingredients()[ingredient_index]
        assert ingredient.get_price() == expected_price