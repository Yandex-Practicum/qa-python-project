from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        assert available_buns
        assert all(isinstance(bun, Bun) for bun in available_buns)

    def test_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert available_ingredients
        assert all(isinstance(ingredient, Ingredient) for ingredient in available_ingredients)

    def test_default_buns(self):
        database = Database()
        assert len(database.buns) == 3
        assert all(isinstance(bun, Bun) for bun in database.buns)

    def test_default_ingredients(self):
        database = Database()
        assert len(database.ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in database.ingredients)

    def test_default_buns_names(self):
        database = Database()
        expected_bun_names = ["black bun", "white bun", "red bun"]
        actual_bun_names = [bun.get_name() for bun in database.buns]
        assert actual_bun_names == expected_bun_names

    def test_default_ingredients_names(self):
        database = Database()
        expected_ingredient_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        actual_ingredient_names = [ingredient.get_name() for ingredient in database.ingredients]
        assert actual_ingredient_names == expected_ingredient_names

    def test_default_ingredients_types(self):
        database = Database()
        expected_sauce_types = [INGREDIENT_TYPE_SAUCE] * 3
        actual_sauce_types = [ingredient.get_type() for ingredient in database.ingredients[:3]]
        assert actual_sauce_types == expected_sauce_types

        expected_filling_types = [INGREDIENT_TYPE_FILLING] * 3
        actual_filling_types = [ingredient.get_type() for ingredient in database.ingredients[3:]]
        assert actual_filling_types == expected_filling_types
