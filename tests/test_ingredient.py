import pytest

import data
from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price_ingredient_got_correct_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                data.INGREDIENTS_NAME[0],
                                data.INGREDIENTS_PRICE[0])
        assert ingredient.get_price() == data.INGREDIENTS_PRICE[0]

    def test_get_name_ingredient_got_correct_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING,
                                data.INGREDIENTS_NAME[1],
                                data.INGREDIENTS_PRICE[1])
        assert ingredient.get_name() == data.INGREDIENTS_NAME[1]

    @pytest.mark.parametrize(
        'ingredient_type, num_ingredient',
        [
            [ingredient_types.INGREDIENT_TYPE_SAUCE, 0],
            [ingredient_types.INGREDIENT_TYPE_FILLING, 1]
        ]
    )
    def test_get_type_ingredient_got_correct_type(self, ingredient_type, num_ingredient):
        ingredient = Ingredient(ingredient_type,
                                data.INGREDIENTS_NAME[num_ingredient],
                                data.INGREDIENTS_PRICE[num_ingredient])
        assert ingredient.get_type() == ingredient_type
