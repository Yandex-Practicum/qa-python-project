
import pytest

import ingredient_types
from database import Database


class TestDatabase:
    @pytest.mark.parametrize(
        'bun_name, bun_price, index',
        [
            ("black bun", 100, 0),
            ("white bun", 200, 1),
            ("red bun", 300, 2)
        ]
    )
    def test_available_buns_bun_in_list(self, bun_name, bun_price, index):
        database = Database()
        buns_list = database.available_buns()

        assert (
                buns_list[index].get_name() == bun_name and
                buns_list[index].get_price() == bun_price
        )

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price, index',
        [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 0),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, "sour cream", 200, 1),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, "chili sauce", 300, 2),
            (ingredient_types.INGREDIENT_TYPE_FILLING, "cutlet", 100, 3),
            (ingredient_types.INGREDIENT_TYPE_FILLING, "dinosaur", 200, 4),
            (ingredient_types.INGREDIENT_TYPE_FILLING, "sausage", 300, 5)
        ]
    )
    def test_available_ingredients_ingredient_in_list(self, ingredient_type, ingredient_name, ingredient_price, index):
        database = Database()
        ingredients_list = database.available_ingredients()

        assert (
                ingredients_list[index].get_type() == ingredient_type and
                ingredients_list[index].get_name() == ingredient_name and
                ingredients_list[index].get_price() == ingredient_price
        )
