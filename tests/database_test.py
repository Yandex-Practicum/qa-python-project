from bun import Bun
from ingredient import Ingredient


class TestDatebase:

    def test_available_buns(self, database):
        available_buns = database.available_buns()
        assert all(isinstance(item, Bun) for item in available_buns) == True

    def test_available_ingredients(self, database):
        available_ingredients = database.available_ingredients()
        assert all(isinstance(item, Ingredient)
                   for item in available_ingredients) == True
