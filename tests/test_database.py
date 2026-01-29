from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDataBase:

    def test_available_buns(self):
        database = Database()
        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ]

        result = {}
        for bun in database.available_buns():
            result[bun.get_name()] = bun.get_price()

        for name, price in expected_buns:
            assert result[name] == price

    def test_available_ingredients(self):
        database = Database()
        expected_ingredients = [
            ("hot sauce", INGREDIENT_TYPE_SAUCE, 100),
            ("sour cream", INGREDIENT_TYPE_SAUCE, 200),
            ("chili sauce", INGREDIENT_TYPE_SAUCE, 300),
            ("cutlet", INGREDIENT_TYPE_FILLING, 100),
            ("dinosaur", INGREDIENT_TYPE_FILLING, 200),
            ("sausage", INGREDIENT_TYPE_FILLING, 300),
        ]
        result = {}
        for ingredient in database.available_ingredients():
            result[ingredient.get_name()] = (ingredient.get_type(), ingredient.get_price())

        for name, tp, price in expected_ingredients:
            assert result[name] == (tp, price)



