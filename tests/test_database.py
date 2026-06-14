from Diplom_1.database import Database

class TestDatabase:
    def test_available_buns(self):
        DB = Database()
        assert len(DB.available_buns()) == 3 and DB.available_buns()[0].get_name() == "black bun"

    def test_available_ingredients(self):
        DB = Database()
        assert len(DB.available_ingredients()) == 6 and DB.available_ingredients()[0].get_name() == "hot sauce"