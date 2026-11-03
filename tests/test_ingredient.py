import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestIngredient:
    """Тесты для класса Ingredient."""

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200.5),
            (INGREDIENT_TYPE_FILLING, "cutlet", 99.99),
            (INGREDIENT_TYPE_FILLING, "", 0),
            (INGREDIENT_TYPE_SAUCE, "длинное название соуса", 1e3),
        ],
        ids=[
            "sauce_standard",
            "sauce_float",
            "filling_float",
            "filling_empty_zero",
            "sauce_long_exp",
        ],
    )
    def test_ingredient_stores_and_returns_data(
        self, ingredient_type, name, price
    ):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price