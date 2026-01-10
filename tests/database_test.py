import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize("bun_name, price, index", [
        ("black bun", 100, 0),
        ("white bun", 200, 1),
        ("red bun", 300, 2)
    ])
    def test_available_buns_list_has_correct_bun(self, bun_name, price, index):
        database = Database()
        buns_list = database.available_buns()
        assert (
                buns_list[index].get_name() == bun_name and
                buns_list[index].get_price() == price
        )

    @pytest.mark.parametrize("ingredient_type, ingredient_name, price, index", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200, 1),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300, 2),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100, 3),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200, 4),
        (INGREDIENT_TYPE_FILLING, "sausage", 300, 5)
    ])
    def test_available_ingredients_list_has_correct_ingredient(self, ingredient_type, ingredient_name, price, index):
        database = Database()
        ingredients_list = database.available_ingredients()
        assert (
                ingredients_list[index].get_type() == ingredient_type and
                ingredients_list[index].get_name() == ingredient_name and
                ingredients_list[index].get_price() == price
        )
