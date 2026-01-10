from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestsDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        expected_buns = ["black bun", "white bun", "red bun"]

        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert all(bun.name in expected_buns for bun in buns)

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        expected_ingredients = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        assert all(ingredient.name in expected_ingredients for ingredient in ingredients)
