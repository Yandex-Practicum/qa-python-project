import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestIngredient:
    """Тесты для класса Ingredient."""

    def test_get_type_sauce_type_returns_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_filling_type_returns_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_get_name_valid_name_returns_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_name() == "hot sauce"

    def test_get_name_empty_name_returns_empty_string(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "", 100.0)
        assert ingredient.get_name() == ""

    def test_get_price_valid_price_returns_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_price() == 100.0

    def test_get_price_zero_price_returns_zero(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 0.0)
        assert ingredient.get_price() == 0.0

    def test_get_price_float_price_returns_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 99.99)
        assert ingredient.get_price() == pytest.approx(99.99)

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
            (INGREDIENT_TYPE_FILLING, "sausage", 300.0),
        ],
    )
    def test_constructor_valid_args_stores_values(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_two_ingredients_different_values_are_independent(self):
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200.0)
        assert ingredient1.get_type() != ingredient2.get_type()
        assert ingredient1.get_name() != ingredient2.get_name()
        assert ingredient1.get_price() != ingredient2.get_price()