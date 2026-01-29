from ..praktikum.database import Database
class TestDatabase:

    def test_check_ingredients(self):
        database = Database()

        assert len(database.available_ingredients()) == 6

    def test_check_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

