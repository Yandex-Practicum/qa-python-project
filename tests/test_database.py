from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_list(self, database):
        assert isinstance(database.available_buns(), list)

    def test_available_buns_has_correct_length(self, database):
        assert len(database.available_buns()) == 3

    def test_available_buns_has_correct_names(self, database):
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients_returns_list(self, database):
        assert isinstance(database.available_ingredients(), list)

    def test_available_ingredients_has_correct_length(self, database):
        assert len(database.available_ingredients()) == 6

    def test_available_ingredients_first_three_are_sauces(self, database):
        ingredients = database.available_ingredients()
        for i in range(3):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_SAUCE

    def test_available_ingredients_last_three_are_fillings(self, database):
        ingredients = database.available_ingredients()
        for i in range(3, 6):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_FILLING

    def test_available_ingredients_has_correct_names(self, database):
        actual = [ing.get_name() for ing in database.available_ingredients()]
        expected_ingredient_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        assert actual == expected_ingredient_names
