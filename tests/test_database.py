from Diplom_1.data import DataForTests
from Diplom_1.database import Database


class TestDatabase:

    def test_available_buns_successfully(self):
        data = Database()
        buns = data.available_buns()
        assert buns[0].name == DataForTests.BLACK_BUN

    def test_available_ingredients_successfully(self):
        data = Database()
        ingredients = data.available_ingredients()
        assert ingredients[0].name == DataForTests.HOT_SAUSE
