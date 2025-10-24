import pytest
from tests import data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price_returns_correct_price(self):
        ingredient = Ingredient(
            data.IngredientData.HOT_SAUCE["type"],
            data.IngredientData.HOT_SAUCE["name"],
            data.IngredientData.HOT_SAUCE["price"]
        )
        assert ingredient.get_price() == data.IngredientData.HOT_SAUCE["price"]

    def test_get_name_returns_correct_name(self):
        ingredient = Ingredient(
            data.IngredientData.CUTLET["type"],
            data.IngredientData.CUTLET["name"],
            data.IngredientData.CUTLET["price"]
        )
        assert ingredient.get_name() == data.IngredientData.CUTLET["name"]

    def test_get_type_returns_correct_type_sauce(self):
        ingredient = Ingredient(
            data.IngredientData.SOUR_CREAM["type"],
            data.IngredientData.SOUR_CREAM["name"],
            data.IngredientData.SOUR_CREAM["price"]
        )
        assert ingredient.get_type() == data.IngredientData.SOUR_CREAM["type"]

    def test_get_type_returns_correct_type_filling(self):
        ingredient = Ingredient(
            data.IngredientData.DINOSAUR["type"],
            data.IngredientData.DINOSAUR["name"],
            data.IngredientData.DINOSAUR["price"]
        )
        assert ingredient.get_type() == data.IngredientData.DINOSAUR["type"]

    def test_ingredient_with_minimal_price(self):
        ingredient = Ingredient(
            data.IngredientData.MINIMAL_SAUCE["type"],
            data.IngredientData.MINIMAL_SAUCE["name"],
            data.IngredientData.MINIMAL_SAUCE["price"]
        )
        assert ingredient.get_price() == data.IngredientData.MINIMAL_SAUCE["price"]
