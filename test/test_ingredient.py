import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Сыр", 50)
        assert ingredient.get_type() == ingredient_type

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == "Сыр"

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 50
