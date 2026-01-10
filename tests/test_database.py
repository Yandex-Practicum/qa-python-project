# Database Class tests
from data import BUNS_DATA, INGR_DATA
from utils import get_buns_data, get_ingredients_data


class TestDatabase:

    def test_init_attr_buns_takes_list_of_buns(self, test_database):
        assert (
                isinstance(test_database.buns, list) and
                get_buns_data(test_database.buns) == BUNS_DATA
        )

    def test_init_attr_ingredients_takes_list_of_ingredients(self, test_database):
        ingredients = test_database.ingredients
        assert (
                isinstance(ingredients, list) and
                get_ingredients_data(ingredients) == INGR_DATA
        )

    def test_available_buns_returns_list_of_buns(self, test_database):
        buns = test_database.available_buns()
        assert isinstance(buns, list) and buns == test_database.buns

    def test_available_ingredients_returns_list_of_ingredients(self, test_database):
        ingredients = test_database.available_ingredients()
        assert (
                isinstance(ingredients, list) and
                ingredients == test_database.ingredients
        )
