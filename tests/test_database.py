from praktikum.database import Database

from data import Data


class TestDatabase:


    def test_available_buns(self):

        database = Database()

        buns = database.available_buns()

        assert len(buns) == 3
        assert buns[0].get_name() == Data.BLACK_BUN


    def test_available_ingredients(self):

        database = Database()

        ingredients = database.available_ingredients()

        assert len(ingredients) == 6
        assert ingredients[0].get_name() == Data.HOT_SAUCE