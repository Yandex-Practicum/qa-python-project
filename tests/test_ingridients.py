import pytest

from helpers import SAUCE_NAME, FILLING_NAME, SAUCE_PRICE, FILLING_PRICE
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)
    ])
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, f"Тип ингредиента '{ingredient.get_type()}' не соответствует ожидаемому '{ingredient_type}'"

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)
    ])
    def test_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, f"Название ингредиента '{ingredient.get_name()}' не соответствует ожидаемому '{name}'"

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)
    ])
    def test_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, f"Цена ингредиента {ingredient.get_price()} не соответствует ожидаемой {price}"
