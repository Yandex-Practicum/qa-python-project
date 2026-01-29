import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize("type_of_ingredient, ingredient_name, ingredient_price", [
        (INGREDIENT_TYPE_FILLING, "Астероидная котлета", 6),
        (INGREDIENT_TYPE_SAUCE, "Соус - Абсолютный ноль", 0),
    ])
    def test_ingredient_get_type(self, type_of_ingredient, ingredient_name, ingredient_price):
        ingredient = Ingredient(type_of_ingredient, ingredient_name, ingredient_price)
        assert ingredient.get_type() == type_of_ingredient

    @pytest.mark.parametrize("type_of_ingredient, ingredient_name, ingredient_price", [
        (INGREDIENT_TYPE_FILLING, "Астероидная котлета", 6),
        (INGREDIENT_TYPE_SAUCE, "Соус - Абсолютный ноль", 0),
    ])
    def test_ingredient_get_name(self, type_of_ingredient, ingredient_name, ingredient_price):
        ingredient = Ingredient(type_of_ingredient, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize("type_of_ingredient, ingredient_name, ingredient_price", [
        (INGREDIENT_TYPE_FILLING, "Астероидная котлета", 6),
        (INGREDIENT_TYPE_SAUCE, "Соус - Абсолютный ноль", 0),
    ])
    def test_ingredient_get_price(self, type_of_ingredient, ingredient_name, ingredient_price):
        ingredient = Ingredient(type_of_ingredient, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price
