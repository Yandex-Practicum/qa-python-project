import pytest

import data
import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient():

    def test_get_type_positive_value(self, mock_ingredient):
        testingredient = Ingredient(mock_ingredient.type, mock_ingredient.name, mock_ingredient.price)
        assert testingredient.get_type() == data.DEF_INGREDIENT_TYPE, "Не корректный метод get_type"

    def test_get_mame_positive_value(self, mock_ingredient):
        testingredient = Ingredient(mock_ingredient.type, mock_ingredient.name, mock_ingredient.price)
        assert testingredient.get_name() == data.DEF_INGREDIENT_NAME, "Не корректный метод get_name"

    def test_get_price_positive_value(self, mock_ingredient):
        testingredient = Ingredient(mock_ingredient.type, mock_ingredient.name, mock_ingredient.price)
        assert testingredient.get_price() == data.DEF_INGREDIENT_PRICE, "Не корректный метод get_price"
