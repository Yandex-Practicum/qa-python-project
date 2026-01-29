from praktikum.database import Database

class TestDatabase():
    def test_available_buns(self):
        data = Database()
        buns = data.available_buns()
        assert buns[0].name == "black bun"

    def test_available_ingredients(self):
        data = Database()
        ingredients = data.available_ingredients()
        assert ingredients[0].name == "hot sauce"
