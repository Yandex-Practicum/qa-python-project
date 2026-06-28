from database import Database

from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_available_buns_init_buns_in_database(self):

        db = Database()
        buns = db.available_buns()


        actual_pairs = [(bun.get_name(), bun.get_price()) for bun in buns]

        expected_pairs = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ]

        assert actual_pairs == expected_pairs     

    def test_available_ingredients_init_in_database(self):
        db = Database()
        ingredients = db.available_ingredients()

        actual = [
            (ing.get_type(), ing.get_name(), ing.get_price())
            for ing in ingredients
        ]

        # Ожидаемый набор — ровно в том порядке, как они добавлены в __init__
        expected = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]

        assert actual == expected