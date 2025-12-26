import pytest
from praktikum import ingredient_types
from praktikum.database import Database

class TestDatabase:
    @pytest.mark.parametrize(
        'expected_bun_name, expected_bun_price, bun_index',
        [
            ("black bun", 100, 0),
            ("white bun", 200, 1),
            ("red bun", 300, 2)
        ]
    )
    def test_buns_list_contains_expected_buns(self, expected_bun_name, expected_bun_price, bun_index):
        database = Database()
        buns_list = database.available_buns()

        assert (
            buns_list[bun_index].get_name() == expected_bun_name and
            buns_list[bun_index].get_price() == expected_bun_price
        )

    @pytest.mark.parametrize(
        'expected_ingredient_type, expected_ingredient_name, expected_ingredient_price, ingredient_index',
        [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 0),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, "sour cream", 200, 1),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, "chili sauce", 300, 2),
            (ingredient_types.INGREDIENT_TYPE_FILLING, "cutlet", 100, 3),
            (ingredient_types.INGREDIENT_TYPE_FILLING, "dinosaur", 200, 4),
            (ingredient_types.INGREDIENT_TYPE_FILLING, "sausage", 300, 5)
        ]
    )
    def test_ingredients_list_contains_expected_ingredients(self, expected_ingredient_type, expected_ingredient_name, expected_ingredient_price, ingredient_index):
        database = Database()
        ingredients_list = database.available_ingredients()

        assert (
            ingredients_list[ingredient_index].get_type() == expected_ingredient_type and
            ingredients_list[ingredient_index].get_name() == expected_ingredient_name and
            ingredients_list[ingredient_index].get_price() == expected_ingredient_price
        )
