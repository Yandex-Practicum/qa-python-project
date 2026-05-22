import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type,name,price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 300),
        ],
    )
    def test_get_price_returns_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        "ingredient_type,name,price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 300),
        ],
    )
    def test_get_name_returns_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "ingredient_type,name,price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 300),
        ],
    )
    def test_get_type_returns_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
