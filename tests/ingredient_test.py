import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from tests.test_data import INGREDIENT_NAME, INGREDIENT_PRICE


class TestIngredient:
    def test_get_price_returns_ingredient_price(self, ingredient):
        assert ingredient.get_price() == INGREDIENT_PRICE

    def test_get_name_returns_ingredient_name(self, ingredient):
        assert ingredient.get_name() == INGREDIENT_NAME

    @pytest.mark.parametrize(
        "ingredient_type",
        [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING],
    )
    def test_get_type_returns_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, INGREDIENT_NAME, INGREDIENT_PRICE)

        assert ingredient.get_type() == ingredient_type
