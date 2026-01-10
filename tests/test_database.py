from praktikum.database import Database


class TestDatabaseFunction:
    def test_receive_available_buns(self):
        data = Database()
        buns = data.available_buns()
        assert len(buns) == 3

    def test_receive_available_ingredients(self):
        data = Database()
        buns = data.available_ingredients()
        assert len(buns) == 6