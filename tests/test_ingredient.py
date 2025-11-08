import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize(
        "ing_type, name, price, expected_type",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200, INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100, INGREDIENT_TYPE_FILLING),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200, INGREDIENT_TYPE_FILLING),
            (INGREDIENT_TYPE_FILLING, "sausage", 300, INGREDIENT_TYPE_FILLING),
            ("CUSTOM", "strange", 0.0, "CUSTOM"),
        ],
    )
    def test_get_type(self, ing_type, name, price, expected_type):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize(
        "name, price",
        [
            ("hot sauce", 100),
            ("sour cream", 200),
            ("cutlet", 100),
            ("dinosaur", 200),
            ("sausage", 300),
            ("strange", 0.0),
        ],
    )
    def test_get_name(self, name, price):
        ingredient = Ingredient("IGNORED", name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("hot sauce", 100),
            ("sour cream", 200),
            ("cutlet", 100),
            ("dinosaur", 200),
            ("sausage", 300),
            ("strange", 0.0),
        ],
    )
    def test_get_price(self, name, price):
        ingredient = Ingredient("IGNORED", name, price)
        assert ingredient.get_price() == price
