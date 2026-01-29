from database import Database

class TestDatabase:
    def test_all_buns(self):
        data = Database()
        assert data.available_buns() == data.buns

    def test_all_ingredients(self):
        data = Database()
        assert data.available_ingredients() == data.ingredients
