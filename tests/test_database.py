from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns_returns_non_empty_list(self):
        database = Database()
        buns = database.available_buns()

        assert buns

    def test_available_buns_returns_bun_objects(self):
        database = Database()
        buns = database.available_buns()

        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_non_empty_list(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients

    def test_available_ingredients_returns_ingredient_objects(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert all(isinstance(item, Ingredient) for item in ingredients)

    def test_first_bun_name_is_black_bun(self):
        database = Database()
        buns = database.available_buns()

        assert buns[0].get_name() == 'black bun'

    def test_first_bun_price_is_100(self):
        database = Database()
        buns = database.available_buns()

        assert buns[0].get_price() == 100

    def test_second_bun_name_is_white_bun(self):
        database = Database()
        buns = database.available_buns()

        assert buns[1].get_name() == 'white bun'

    def test_second_bun_price_is_200(self):
        database = Database()
        buns = database.available_buns()

        assert buns[1].get_price() == 200

    def test_first_ingredient_type_is_sauce(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[0].get_type() == 'SAUCE'

    def test_first_ingredient_name_is_hot_sauce(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[0].get_name() == 'hot sauce'

    def test_first_ingredient_price_is_100(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[0].get_price() == 100

    def test_last_ingredient_type_is_filling(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[-1].get_type() == 'FILLING'

    def test_last_ingredient_name_is_sausage(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[-1].get_name() == 'sausage'

