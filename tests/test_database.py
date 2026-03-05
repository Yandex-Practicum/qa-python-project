
class TestDatabase:
    def test_available_buns_returns_list_of_buns(self, db):
        available_buns = db.available_buns()

        assert len(available_buns) == 3
        assert isinstance(available_buns, list)


    def test_available_ingredients_returns_list_of_ingredients(self, db):
        available_ingredients = db.available_ingredients()

        assert len(available_ingredients) == 6
        assert isinstance(available_ingredients, list)


