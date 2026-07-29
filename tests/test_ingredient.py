import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type",
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING
        ]
    )
    def test_get_type_returns_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "ketchup", 50)
        assert ingredient.get_type() == ingredient_type


    def test_get_name_returns_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,"ketchup",50)
        assert ingredient.get_name() == "ketchup"


    def test_get_price_returns_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,"ketchup",50)
        assert ingredient.get_price() == 50