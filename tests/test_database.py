from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) > 0

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) > 0
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(sauces) > 0
        assert len(fillings) > 0
