from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_first_bun(self, mock_database):
        first_bun = mock_database.available_buns()[0]
        assert first_bun.get_name() == "black bun"

    def test_first_ingredient_type(self, mock_database):
        first_ingredient = mock_database.available_ingredients()[0]
        assert first_ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_last_ingredient_type(self, mock_database):
        last_ingredient = mock_database.available_ingredients()[-1]
        assert last_ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_last_ingredient(self, mock_database):
            last_ingredient = mock_database.available_ingredients()[-1]
            assert last_ingredient.get_name() == "sausage"
