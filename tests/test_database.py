from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:
    def test_available_buns_returns_buns(self, database):
        buns = database.available_buns()

        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_ingredients(self, database):
        ingredients = database.available_ingredients()

        assert isinstance(ingredients, list)
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
