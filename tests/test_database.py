from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_database_initialization(self):
        database = Database()

    def test_buns(self):
        database = Database()
        assert len(database.buns) == 3
        assert isinstance(database.buns[0], Bun)
        assert database.buns[0].get_name() == "black bun"
        assert database.buns[1].get_name() == "white bun"
        assert database.buns[2].get_name() == "red bun"

    def test_ingredients(self):
        database = Database()
        assert len(database.ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in database.ingredients)

    def test_sauces(self):
        database = Database()
        sauces = [ingredient for ingredient in database.ingredients if ingredient.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        assert {sauce.get_name() for sauce in sauces} == {"hot sauce", "sour cream", "chili sauce"}

    def test_fillings(self):
        database = Database()
        fillings = [ingredient for ingredient in database.ingredients if ingredient.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
        assert {filling.get_name() for filling in fillings} == {"cutlet", "dinosaur", "sausage"}

    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns == database.buns

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        assert ingredients == database.ingredients