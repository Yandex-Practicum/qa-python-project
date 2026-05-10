from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
        
    def test_available_buns(self):
        database = Database()
        database.buns = [Bun("black bun", 100)]
        list = database.available_buns()
        assert list[0].get_name() == "black bun"
        
    def test_available_ingredients(self):
        database = Database()
        database.ingredient = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)]
        list = database.available_ingredients()
        assert list[0].get_name() == "hot sauce"
