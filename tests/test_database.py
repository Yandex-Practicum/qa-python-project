from praktikum.database import Database

class TestDatabase:

    def test_avialable_buns_return_correct_count_and_data(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_avilable_ingredients_return_correct_count_and_data(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_type() == "SAUCE"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_type() == "FILLING"