import pytest

from data import Data
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestDatabase:

    # проверка, что available_buns возвращает список всех булок
    @pytest.mark.parametrize(
        'name, price',
        [
            (Data.BUN_1, Data.BUN_1_PRICE),
            (Data.BUN_2, Data.BUN_2_PRICE),
            (Data.BUN_3, Data.BUN_3_PRICE)
        ]
    )
    def test_available_buns_returns_all_buns(self, name, price, database):
        buns = database.available_buns()
        found = False
        
        for bun in buns:
            if bun.name == name:
                assert bun.price == price
                found = True

        assert found

    # проверка что available_ingredients возвращает список всех ингредиентов
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
    def test_available_ingredients_returns_all_ingredients(self, ingredient_type, name, price, database): 
        ingredients = database.available_ingredients()
        found = False

        for ingredient in ingredients:
            if ingredient.type == ingredient_type and ingredient.name == name:
                assert ingredient.price == price
                found = True

        assert found
        