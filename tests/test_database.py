import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize('index, name_bun, price_bun',
                             [   [0, "black bun", 100],
                                 [1, "white bun", 200],
                                 [2, "red bun", 300] ])
    def test_available_buns(self, index, name_bun, price_bun):

        db = Database()
        available_buns = db.available_buns()

        assert available_buns[index].get_name() == name_bun
        assert available_buns[index].get_price() == price_bun

    @pytest.mark.parametrize('index, name_ingredient, price_ingredient',
                             [[0, "hot sauce", 100],
                              [1, "sour cream", 200],
                              [2, "chili sauce", 300],
                              [3, "cutlet", 100],
                              [4, "dinosaur", 200],
                              [5, "sausage", 300] ])
    def test_available_ingredients(self, index, name_ingredient, price_ingredient):

        db = Database()
        available_ingredients = db.available_ingredients()

        assert available_ingredients[index].get_name() == name_ingredient
        assert available_ingredients[index].get_price() == price_ingredient
        if index < 3:
            assert available_ingredients[index].get_type() == INGREDIENT_TYPE_SAUCE
        else:
            assert available_ingredients[index].get_type() == INGREDIENT_TYPE_FILLING