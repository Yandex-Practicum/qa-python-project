import pytest

from ingredient import Ingredient


class TestIngredient:

    def test_get_price_returns_price(self):
        ingredient = Ingredient("sauce", "ketchup", 50)

        assert ingredient.get_price() == 50

    def test_get_name_returns_name(self):
        ingredient = Ingredient("sauce", "ketchup", 50)

        assert ingredient.get_name() == "ketchup"

    def test_get_type_returns_type(self):
        ingredient = Ingredient("sauce", "ketchup", 50)

        assert ingredient.get_type() == "sauce"
