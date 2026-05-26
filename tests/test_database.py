from praktikum.database import Database
#python -B -m pytest tests/test_database.py

class TestDatabase:
    def test_available_buns(self):
        buns = Database()
        assert len(buns.available_buns()) == 3

    def test_available_ingredients(self):
        ingredient = Database()
        assert len(ingredient.available_ingredients()) == 6