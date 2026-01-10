from praktikum.database import Database


class TestDB:

    def test_db_buns(self):
        db = Database()
        bun_item = db.available_buns()[0]
        assert 'black bun' == bun_item.get_name()

    def test_db_ingredients(self):
        db = Database()
        ingredients_item = db.available_ingredients()[0]
        assert 'hot sauce' == ingredients_item.get_name()