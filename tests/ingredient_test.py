import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)
from tests.test_data import (
    SAUCE_NAME,
    SAUCE_PRICE,
    FILLING_NAME,
    FILLING_PRICE,
)


class TestIngredientGetType:
    """Тесты метода get_type."""

    @pytest.mark.parametrize(
        "ingredient_type",
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING,
        ],
    )
    def test_get_type_returns_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, SAUCE_NAME, SAUCE_PRICE)
        assert ingredient.get_type() == ingredient_type


class TestIngredientGetName:
    """Тесты метода get_name."""

    @pytest.mark.parametrize(
        "name",
        [
            "hot sauce",
            "sour cream",
            "cutlet",
            "dinosaur",
            "",
        ],
    )
    def test_get_name_returns_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, SAUCE_PRICE)
        assert ingredient.get_name() == name


class TestIngredientGetPrice:
    """Тесты метода get_price."""

    @pytest.mark.parametrize(
        "price",
        [
            0.0,
            100.0,
            200.0,
            300.0,
        ],
    )
    def test_get_price_returns_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, price)
        assert ingredient.get_price() == price