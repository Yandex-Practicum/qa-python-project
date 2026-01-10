import pytest

class TestDatabase:
    def test_available_buns(self, database, buns_data):
        buns = database.available_buns()
        assert len(buns) == len(buns_data)

        for bun, expected in zip(buns, buns_data):
            assert bun.get_name() == expected["name"]
            assert bun.get_price() == expected["price"]

    def test_available_ingredients(self, database, ingredient_list_data):
        ingredients = database.available_ingredients()
        assert len(ingredients) == len(ingredient_list_data)

        for ingredient, expected in zip(ingredients, ingredient_list_data):
            assert ingredient.get_type() == expected["type"]
            assert ingredient.get_name() == expected["name"]
            assert ingredient.get_price() == expected["price"]