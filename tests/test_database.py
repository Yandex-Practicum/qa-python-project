from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns_returns_buns_list(self, database):
        buns = database.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_ingredients_list(self, database):
        ingredients = database.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
