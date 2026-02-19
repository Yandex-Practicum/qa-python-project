from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3

        names = []
        for bun in buns:
            names.append(bun.get_name())

        assert names == ['black bun', 'white bun', 'red bun']

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

    def test_ingredient_types_count(self):
        db = Database()
        ingredients = db.available_ingredients()

        sauce_count = 0
        filling_count = 0

        for ing in ingredients:
            if ing.get_type() == INGREDIENT_TYPE_SAUCE:
                sauce_count += 1

            if ing.get_type() == INGREDIENT_TYPE_FILLING:
                filling_count += 1

        assert sauce_count == 3
        assert filling_count == 3
