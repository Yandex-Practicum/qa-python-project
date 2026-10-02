import pytest

from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestIngredient:

    # проверка, что get_type возвращает тип ингредиента
    @pytest.mark.parametrize(
        'ingredient_type, name, price', 
        [
            (INGREDIENT_TYPE_SAUCE, Data.SAUCE_1, Data.SAUCE_1_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.SAUCE_2, Data.SAUCE_2_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.SAUCE_3, Data.SAUCE_3_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.FILLING_1, Data.FILLING_1_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.FILLING_2, Data.FILLING_2_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.FILLING_3, Data.FILLING_3_PRICE)
        ]
    )
    def test_get_type_returns_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type


    # проверка, что get_name возвращает название ингредиента
    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            (INGREDIENT_TYPE_SAUCE, Data.SAUCE_1, Data.SAUCE_1_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.FILLING_1, Data.FILLING_1_PRICE)
        ]
    )
    def test_get_name_returns_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name


    # проверка, что get_price возвращает цену ингредиента
    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            (INGREDIENT_TYPE_SAUCE, Data.SAUCE_2, Data.SAUCE_2_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.FILLING_2, Data.FILLING_2_PRICE)
        ]
    )
    def test_get_price_returns_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price
