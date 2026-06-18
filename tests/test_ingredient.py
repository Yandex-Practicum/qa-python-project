import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_with_valid_type_returns_correct_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "item", 10)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["hot sauce", "cutlet"])
    def test_get_name_with_valid_name_returns_correct_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 10)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [0, 10, 99.99])
    def test_get_price_with_valid_price_returns_correct_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "item", price)

        assert ingredient.get_price() == price
