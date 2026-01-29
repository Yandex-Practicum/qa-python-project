from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()

        assert len(database.available_buns()) == 3
        assert database.available_buns()[1].get_name() == "white bun"
        assert database.available_buns()[1].get_price() == 200

    def test_available_ingredients(self):
        database = Database()

        assert len(database.available_ingredients()) == 6
        assert database.available_ingredients()[1].get_name() == "sour cream"
        assert database.available_ingredients()[1].get_price() == 200
