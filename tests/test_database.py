import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.fixture
    def database(self):
        return Database()

    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)
        assert buns[0].get_name() == 'black bun'
        assert buns[0].get_price() == 100

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)
        assert ingredients[0].get_name() == 'hot sauce'
        assert ingredients[0].get_price() == 100
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE

