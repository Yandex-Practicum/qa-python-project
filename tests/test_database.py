from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_database_has_buns(self):
        database = Database()

        assert len(database.available_buns()) > 0

    def test_available_buns(self):
        database = Database()

        buns = database.available_buns()

        assert buns[0].name == "black bun"
        assert buns[0].price == 100

    def test_available_ingredients(self):
        database = Database()

        ingredients = database.available_ingredients()

        assert ingredients[0].name == "hot sauce"
        assert ingredients[0].price == 100
        assert ingredients[0].type == INGREDIENT_TYPE_SAUCE