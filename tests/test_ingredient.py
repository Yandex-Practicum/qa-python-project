import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import ingredient_cases

class TestIngredient:
    @pytest.mark.parametrize("type_, name, price", ingredient_cases)
    def test_ingredient_type_is_saved(self, type_, name, price):
        ingr = Ingredient(type_, name, price)
        assert ingr.type == type_

    @pytest.mark.parametrize("type_, name, price", ingredient_cases)
    def test_ingredient_name_is_saved(self, type_, name, price):
        ingr = Ingredient(type_, name, price)
        assert ingr.name == name

    @pytest.mark.parametrize("type_, name, price", ingredient_cases)
    def test_ingredient_price_is_saved(self, type_, name, price):
        ingr = Ingredient(type_, name, price)
        assert ingr.price == price

    @pytest.mark.parametrize("type_, name, price", ingredient_cases)
    def test_get_type_returns_real_type(self, type_, name, price):
        ingr = Ingredient(type_, name, price)
        assert ingr.get_type() == type_

    @pytest.mark.parametrize("type_, name, price", ingredient_cases)
    def test_get_name_returns_real_name(self, type_, name, price):
        ingr = Ingredient(type_, name, price)
        assert ingr.get_name() == name

    @pytest.mark.parametrize("type_, name, price", ingredient_cases)
    def test_get_price_returns_real_price(self, type_, name, price):
        ingr = Ingredient(type_, name, price)
        assert ingr.get_price() == price
