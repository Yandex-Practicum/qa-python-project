import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient, expected_name",
        [
            ((INGREDIENT_TYPE_SAUCE, "hot sauce", 100), "hot sauce"),
            ((INGREDIENT_TYPE_FILLING, "cutlet", 200), "cutlet"),
        ],
        indirect=["ingredient"],
    )
    def test_get_name_returns_name(self, ingredient, expected_name):
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize(
        "ingredient, expected_price",
        [
            ((INGREDIENT_TYPE_SAUCE, "hot sauce", 100), 100),
            ((INGREDIENT_TYPE_FILLING, "cutlet", 200), 200),
        ],
        indirect=["ingredient"],
    )
    def test_get_price_returns_price(self, ingredient, expected_price):
        assert ingredient.get_price() == expected_price

    @pytest.mark.parametrize(
        "ingredient, expected_type",
        [
            ((INGREDIENT_TYPE_SAUCE, "hot sauce", 100), INGREDIENT_TYPE_SAUCE),
            ((INGREDIENT_TYPE_FILLING, "cutlet", 200), INGREDIENT_TYPE_FILLING),
        ],
        indirect=["ingredient"],
    )
    def test_get_type_returns_type(self, ingredient, expected_type):
        assert ingredient.get_type() == expected_type
