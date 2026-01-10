from praktikum.database import Database

class TestDatabase:
    def test_available_buns(self):
        data = Database()
        assert len(data.available_buns()) == 3

    def test_available_ingredients(self):
        data = Database()
        assert len(data.available_ingredients()) == 6
