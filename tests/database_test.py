from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:

    def test_init_true(self):
        database = Database()
        base = database.available_buns()
        assert base[0].get_name() == "black bun"

    def test_available_buns(self):
        database = Database()
        base = database.available_buns()
        assert len(base) == 3

    def test_available_ingredient(self):
        database = Database()
        base = database.available_ingredients()
        assert len(base) == 6
         