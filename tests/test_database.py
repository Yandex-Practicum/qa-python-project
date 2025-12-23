import pytest
from data import ExpectedBunNames, ExpectedIngredientNames
from helpers import check_bun_names, check_ingredient_names

class TestDatabase:

    @pytest.mark.parametrize("expected_bun_names", ExpectedBunNames.data)
    def test_available_buns(self, database, expected_bun_names):
        buns = database.available_buns()
        assert check_bun_names(buns, expected_bun_names)

    @pytest.mark.parametrize("expected_ingredient_names", ExpectedIngredientNames.data)
    def test_available_ingredients(self, database, expected_ingredient_names):
        ingredients = database.available_ingredients()
        assert check_ingredient_names(ingredients, expected_ingredient_names)
