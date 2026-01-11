
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns_true(self):
        database = Database()
        database.buns = []
        database.buns.append(Bun("black bun", 100).__dict__)
        database.buns.append(Bun("white bun", 200).__dict__)
        database.buns.append(Bun("red bun", 300).__dict__)

        assert database.buns == [{'name': 'black bun', 'price': 100}, {'name': 'white bun', 'price': 200},
                                 {'name': 'red bun', 'price': 300}]

    def test_available_ingredients_true(self):
        database = Database()
        database.ingredients = []

        database.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100).__dict__)
        database.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200).__dict__)
        database.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300).__dict__)

        database.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100).__dict__)
        database.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200).__dict__)
        database.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300).__dict__)

        assert database.ingredients == [
                   {'type': 'SAUCE', 'name': 'hot sauce', 'price': 100},
                   {'type': 'SAUCE', 'name': 'sour cream', 'price': 200},
                   {'type': 'SAUCE', 'name': 'chili sauce', 'price': 300},
                   {'type': 'FILLING', 'name': 'cutlet', 'price': 100},
                   {'type': 'FILLING', 'name': 'dinosaur', 'price': 200},
                   {'type': 'FILLING', 'name': 'sausage', 'price': 300}
        ]

