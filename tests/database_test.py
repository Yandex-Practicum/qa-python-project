from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Юнит-тесты для класса Database."""

    def test_available_buns(self):
        database = Database()

        buns = database.available_buns()

        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert [bun.get_name() for bun in buns] == ['black bun', 'white bun', 'red bun']
        assert [bun.get_price() for bun in buns] == [100, 200, 300]

    def test_available_ingredients(self):
        database = Database()

        ingredients = database.available_ingredients()

        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        assert [ingredient.get_name() for ingredient in ingredients] == [
            'hot sauce', 'sour cream', 'chili sauce',
            'cutlet', 'dinosaur', 'sausage',
        ]

    def test_available_ingredients_contains_sauces(self):
        database = Database()

        ingredients = database.available_ingredients()

        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_available_ingredients_contains_fillings(self):
        database = Database()

        ingredients = database.available_ingredients()

        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
