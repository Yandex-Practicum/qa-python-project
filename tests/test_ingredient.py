import pytest
from praktikum.ingredient import Ingredient
from tests.constants import ALL_INGREDIENTS


class TestIngredient:

    @pytest.mark.parametrize(
        "name, price, ingredient_type",
        ALL_INGREDIENTS,
    )
    def test_get_name_returns_name(self, name, price, ingredient_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "name, price, ingredient_type",
        ALL_INGREDIENTS,
    )
    def test_get_price_returns_price(self, name, price, ingredient_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        "name, price, ingredient_type",
        ALL_INGREDIENTS,
    )
    def test_get_type_returns_type(self, name, price, ingredient_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type