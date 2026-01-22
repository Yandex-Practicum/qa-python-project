from praktikum.database import Database


class TestDatabase:
    def test_check_of_available_buns_successful(self):
        db = Database()
        return_value = db.available_buns()
        assert len(return_value) == 3

    def test_check_of_available_ingredients_successful(self):
        db = Database()
        return_value = db.available_ingredients()
        assert len(return_value) == 6
