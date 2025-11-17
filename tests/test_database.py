from praktikum.database import Database


class TestDatabase:

    def test_return_correct_buns_from_db(self, get_buns_from_db):
        db = Database()
        available_buns = db.available_buns()
        n = 3

        assert len(available_buns) == n

        for available_bun, bun_from_db in zip(available_buns, get_buns_from_db):
            assert available_bun.get_name() == bun_from_db.get_name()

    def test_return_correct_ingredients_from_db(self, get_ingredients_from_db):
        db = Database()
        available_ingredients = db.available_ingredients()
        n = 6

        assert len(available_ingredients) == n

        for available_ingredient, ingredient_from_db in zip(available_ingredients, get_ingredients_from_db):
            assert available_ingredient.get_name() == ingredient_from_db.get_name()
