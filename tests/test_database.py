from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(b, Bun) for b in buns)
        assert len(buns) == 3

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(i, Ingredient) for i in ingredients)
        assert len(ingredients) == 6