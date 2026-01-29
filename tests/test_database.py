class TestDatabase:
    def test_available_buns(self, database, bun, bun_2):
        assert bun and bun_2 in database.available_buns()

    def test_available_ingredients(self, database,
                                   ingredient, ingredient_2):
        assert ingredient and ingredient_2 in database.available_ingredients()
