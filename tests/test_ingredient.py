import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from test_data import Data


class TestIngredient():

    # Тест init
    def test_ingredient_initialization(self):
        name = Data.INGREDIENT_NAME_SAUCE
        price = Data.INGREDIENT_NAME_SAUCE
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert ingredient.name == name
        assert ingredient.price == price
        assert ingredient.type == INGREDIENT_TYPE_SAUCE

    # Тест метода get_price
    def test_get_price_return_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_NAME_SAUCE, Data.INGREDIENT_NAME_SAUCE)
        assert ingredient.get_price() == Data.INGREDIENT_NAME_SAUCE

    # Тест метода get_name
    def test_get_name_return_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_NAME_SAUCE, Data.INGREDIENT_NAME_SAUCE)
        assert ingredient.get_name() == Data.INGREDIENT_NAME_SAUCE

    # Тест метода get_type
    @pytest.mark.parametrize(
        'type_ingredient, name_ingredient, price_ingredient, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_NAME_SAUCE, Data.INGREDIENT_NAME_SAUCE, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, Data.INGREDIENT_NAME_FILLING, Data.INGREDIENT_PRICE_FILLING, 'FILLING']
        ]
    )
    def test_get_type_return_correct_type(self, type_ingredient, name_ingredient, price_ingredient, expected_ingredient):
        ingredient = Ingredient(type_ingredient, name_ingredient, price_ingredient)
        assert ingredient.get_type() == expected_ingredient
