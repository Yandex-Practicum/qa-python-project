from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_all_buns(self):
        database = Database()

        buns = [(bun.get_name(), bun.get_price()) for bun in database.available_buns()]

        assert buns == [('black bun', 100), ('white bun', 200), ('red bun', 300)]

    def test_available_ingredients_returns_all_ingredients(self):
        database = Database()

        ingredients = [
            (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
            for ingredient in database.available_ingredients()
        ]

        assert ingredients == [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            (INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            (INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
            (INGREDIENT_TYPE_FILLING, 'sausage', 300)
        ]
