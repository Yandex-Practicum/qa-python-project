from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def setup_method(self):
        self.database = Database()

    def test_available_buns_returns_list(self):
        buns = self.database.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_returns_non_empty_list(self):
        buns = self.database.available_buns()
        assert len(buns) > 0

    def test_available_buns_elements_are_bun_instances(self):
        buns = self.database.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_list(self):
        ingredients = self.database.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_returns_non_empty_list(self):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) > 0

    def test_available_ingredients_elements_are_ingredient_instances(self):
        ingredients = self.database.available_ingredients()
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

    def test_available_ingredients_contains_sauce_type(self):
        ingredients = self.database.available_ingredients()
        types = [ing.get_type() for ing in ingredients]
        assert INGREDIENT_TYPE_SAUCE in types

    def test_available_ingredients_contains_filling_type(self):
        ingredients = self.database.available_ingredients()
        types = [ing.get_type() for ing in ingredients]
        assert INGREDIENT_TYPE_FILLING in types