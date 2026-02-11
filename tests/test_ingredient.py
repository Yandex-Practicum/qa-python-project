from praktikum.ingredient import Ingredient
from test_data import INGREDIENT_NAME, INGREDIENT_PRICE, FILLING_NAME, FILLING_PRICE, SAUCE_NAME, SAUCE_PRICE
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredient:

    def test_get_name_returns_correct_name(self, sauce_ingredient: Ingredient):
        assert sauce_ingredient.get_name() == INGREDIENT_NAME

    def test_get_price_returns_correct_price(self, sauce_ingredient: Ingredient):
        assert sauce_ingredient.get_price() == INGREDIENT_PRICE

    def test_get_type_returns_sauce_type(self, sauce_ingredient: Ingredient):
        assert sauce_ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_returns_filling_type(self, filling_ingredient: Ingredient):
        assert filling_ingredient.get_type() == INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type",
        [
            (INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE, INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE, INGREDIENT_TYPE_FILLING),
        ]
    )
    def test_ingredient_properties(
        self,
        ingredient_factory,
        ingredient_type,
        name,
        price,
        expected_type
    ):
        ingredient = ingredient_factory(ingredient_type, name, price)

        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
        assert ingredient.get_type() == expected_type
