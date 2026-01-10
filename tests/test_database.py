from praktikum.database import Database


class TestDatabase:

    def test_available_buns_got_len_list_successfully(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_got_len_list_successfully(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
