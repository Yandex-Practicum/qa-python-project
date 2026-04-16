import pytest

import data
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_price_success(self, ingredient):
        assert ingredient.get_price() == data.ingredient_price

    def test_get_name_success(self, ingredient):
        assert ingredient.get_name() == data.ingredient_name

    @pytest.mark.parametrize(
        "ingredient_requested_type, expected_type",
        [
            (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING)
        ],
        indirect=["ingredient_requested_type"]
    )
    def test_get_type_success(self, ingredient_requested_type, expected_type):
        assert ingredient_requested_type.get_type() == expected_type
