from praktikum.database import Database


class TestDatabase:

    def test_available_buns_returns_correct_count(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_buns_first_name(self):
        database = Database()
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_available_buns_second_name(self):
        database = Database()
        buns = database.available_buns()
        assert buns[1].get_name() == "white bun"

    def test_available_buns_third_name(self):
        database = Database()
        buns = database.available_buns()
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients_returns_correct_count(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_first_name(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"

    def test_available_ingredients_last_name(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[-1].get_name() == "sausage"