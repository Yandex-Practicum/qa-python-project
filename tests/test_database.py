from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self):
        available_buns = {
            "black bun": 100,
            "white bun": 200,
            "red bun": 300
        }
        database = Database()
        database_buns = database.available_buns()

        assert len(available_buns) == len(database_buns)
        for bun in database_buns:
            assert bun.get_name() in available_buns
            assert bun.get_price() == available_buns[bun.get_name()]

    def test_available_ingredients(self):
        available_ingredients = {
            "hot sauce": (INGREDIENT_TYPE_SAUCE, 100),
            "sour cream": (INGREDIENT_TYPE_SAUCE, 200),
            "chili sauce": (INGREDIENT_TYPE_SAUCE, 300),
            "cutlet": (INGREDIENT_TYPE_FILLING, 100),
            "dinosaur": (INGREDIENT_TYPE_FILLING, 200),
            "sausage": (INGREDIENT_TYPE_FILLING, 300),
        }

        database = Database()
        database_ingredients = database.available_ingredients()

        assert len(database_ingredients) == len(available_ingredients)

        for ingredient in database_ingredients:
            assert ingredient.get_name() in available_ingredients

            correct_ingredient_data = available_ingredients[ingredient.get_name()]
            assert ingredient.get_type() == correct_ingredient_data[0]
            assert ingredient.get_price() == correct_ingredient_data[1]