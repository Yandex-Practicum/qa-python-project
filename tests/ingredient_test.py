import pytest

from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:
    ingredients = [
            (ingredient['type'], ingredient['name'], ingredient['price']) for ingredient in Data.INGREDIENTS
    ]
    @pytest.mark.parametrize('type, name, price', ingredients)
    def test_create_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.type == type and ingredient.name == name and ingredient.price == price

    @pytest.mark.parametrize('type, name, price', ingredients)
    def test_get_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        actual_price = ingredient.get_price()

        assert actual_price == price

    @pytest.mark.parametrize('type, name, price', ingredients)
    def test_name_is_str(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        actual_name = ingredient.get_name()

        assert isinstance(actual_name, str)

    @pytest.mark.parametrize('type, name, price', ingredients)
    def test_get_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        actual_type = ingredient.get_type()

        assert actual_type == type
