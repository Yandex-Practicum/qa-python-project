from praktikum.database import Database


class TestDatabase:

    def test_database_available_buns(self):
        test_data = Database()
        assert len(test_data.available_buns()) == 3

    def test_database_available_ingredients(self):
        test_data = Database()
        assert len(test_data.available_ingredients()) == 6
