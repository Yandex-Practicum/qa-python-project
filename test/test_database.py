import pytest

from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_three_buns(self, database):
        buns = database.available_buns()

        assert len(buns) == 3

    @pytest.mark.parametrize("index, name, price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_available_buns_content(self, database, index, name, price):
        bun = database.available_buns()[index]

        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_available_ingredients_returns_six_ingredients(self, database):
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    @pytest.mark.parametrize("index, ingredient_type, name, price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_available_ingredients_content(self, database, index, ingredient_type, name, price):
        ingredient = database.available_ingredients()[index]

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
