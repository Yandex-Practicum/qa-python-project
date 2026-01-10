# class for tests Database methods
class TestsDatabase:

    def test_available_buns(self, new_database):
        assert len(new_database.available_buns()) > 0

    def test_available_ingredients(self, new_database):
        assert len(new_database.available_ingredients()) > 0
