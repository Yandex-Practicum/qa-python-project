import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from tests.conftest import ingredient

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price",
                             [
                                 [INGREDIENT_TYPE_SAUCE, "сырный", 25.0],
                                 [INGREDIENT_TYPE_FILLING, "Чеддер", 50.0]]
                             )
    def test_init_correct_types_and_values(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name = name, price = price)
        assert isinstance(ingredient.type, str)
        assert isinstance(ingredient.name, str)
        assert isinstance(ingredient.price, float)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price


    def test_get_price_returns_price(self, ingredient):
        price = ingredient.get_price()
        assert price == 30.0

    def test_get_name_returns_name(self, ingredient):
        name = ingredient.get_name()
        assert name == "1000 островов"

    def test_get_type_returns_type(self, ingredient):
        result = ingredient.get_type()
        assert result == INGREDIENT_TYPE_SAUCE
