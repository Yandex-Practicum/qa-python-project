from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_type() == "SAUCE"
        assert ingredients[0].get_price() == 100
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_type() == "FILLING"
        assert ingredients[3].get_price() == 100