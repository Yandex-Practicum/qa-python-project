from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(bun.get_price() > 0 for bun in buns)

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        types = [i.get_type() for i in ingredients]
        assert INGREDIENT_TYPE_SAUCE in types
        assert INGREDIENT_TYPE_FILLING in types
