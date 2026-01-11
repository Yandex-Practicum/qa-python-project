from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from data import TestData
import pytest


class TestIngredient:

    @pytest.mark.parametrize('price',
                             [TestData.BUN_PRICE_VALID, TestData.BUN_PRICE_FLOAT])
    def test_get_price_successful(self, price):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME_CHILI, price)
        assert ingredient.get_price() == price

    def test_get_price_unsuccessful(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME_CHILI, TestData.BUN_PRICE_LESS_THAN_ZERO)
        assert ingredient.get_price() != TestData.BUN_PRICE_LESS_THAN_ZERO

    def test_get_name_of_sauce_successful(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME_CHILI, TestData.BUN_PRICE_VALID)
        assert ingredient.get_name() == TestData.SAUCE_NAME_CHILI

    def test_get_name_of_filling_successful(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, TestData.FILLING_NAME_SAUSAGE, TestData.BUN_PRICE_VALID)
        assert ingredient.get_name() == TestData.FILLING_NAME_SAUSAGE

    @pytest.mark.parametrize('ingredient_type',
                             [ingredient_types.INGREDIENT_TYPE_SAUCE, ingredient_types.INGREDIENT_TYPE_FILLING])
    def test_get_type_successful(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, TestData.SAUCE_NAME_CHILI, TestData.BUN_PRICE_VALID)
        assert ingredient.get_type() == ingredient_type
