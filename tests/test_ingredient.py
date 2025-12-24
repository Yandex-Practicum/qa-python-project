import pytest
from praktikum.ingredient import Ingredient
import data
from praktikum.ingredient_types import *
import logging
logging.basicConfig(level=logging.INFO)


class TestIngredient:

    @pytest.mark.parametrize('ingredient_maket, expected_type, expected_name, expected_price', [
        (Ingredient(INGREDIENT_TYPE_SAUCE, data.INGREDIENT_NAME_SAUCE, data.INGREDIENT_PRICE_SAUCE),
         INGREDIENT_TYPE_SAUCE, data.INGREDIENT_NAME_SAUCE, data.INGREDIENT_PRICE_SAUCE),
        (Ingredient(INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_FILLING, data.INGREDIENT_PRICE_FILLING),
         INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_FILLING, data.INGREDIENT_PRICE_FILLING)])
    def test_ingredient_constructor_true(self, ingredient_maket, expected_type, expected_name, expected_price):
        ingredient = ingredient_maket
        assert (ingredient.type == expected_type and ingredient.name == expected_name and
                ingredient.price == expected_price), \
            (f"\nОжидалось имя: {expected_name}, но получено: {ingredient.name}" and
             f"\nОжидалась цена: {expected_price}, но получено: {ingredient.price}")
        logging.info(f"\nТестируемый ингридиент: имя = {ingredient.name}, цена = {ingredient.price}")

    def test_get_type_ingredient_true(self, create_ingredient):
        assert create_ingredient.get_type() == create_ingredient.type
        logging.info(f'\nТип ингредиента: {create_ingredient.type}')

    def test_get_name_ingredient_true(self, create_ingredient):
        assert create_ingredient.get_name() == create_ingredient.name
        logging.info(f'\nИмя ингредиента: {create_ingredient.name}')

    def test_get_price_ingredient_true(self, create_ingredient):
        assert create_ingredient.get_price() == create_ingredient.price
        logging.info(f'\nЦена ингредиента: {create_ingredient.price}')
