from praktikum.database import Database

class TestDatabase:
    def test_available_buns(self):
        data = Database()
        assert data.buns == data.available_buns()

    def test_available_ingredients(self):
        data = Database()
        assert data.ingredients == data.available_ingredients()