import pytest
import data
import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient:


    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, data.NAME_ASTROSAUCE, data.PRICE_ASTROSAUCE),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, data.NAME_COSMOSAUCE, data.PRICE_COSMOSAUCE),
            (ingredient_types.INGREDIENT_TYPE_FILLING,data.NAME_FILLING_VULKAN_CUTLET, data.PRICE_VULKAN_CUTLET),
            (ingredient_types.INGREDIENT_TYPE_FILLING,data.NAME_FILLING_SALAD_MARS, data.PRICE_SALAD_MARS),
        ]
    )
    def test_get_price_one_ingredient_return_correct_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, data.NAME_ASTROSAUCE, data.PRICE_ASTROSAUCE),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, data.NAME_COSMOSAUCE, data.PRICE_COSMOSAUCE),
            (ingredient_types.INGREDIENT_TYPE_FILLING,data.NAME_FILLING_VULKAN_CUTLET, data.PRICE_VULKAN_CUTLET),
            (ingredient_types.INGREDIENT_TYPE_FILLING,data.NAME_FILLING_SALAD_MARS, data.PRICE_SALAD_MARS),
        ]
    )
    def test_get_name_should_return_correct_name_for_filling(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, data.NAME_ASTROSAUCE, data.PRICE_ASTROSAUCE),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, data.NAME_COSMOSAUCE, data.PRICE_COSMOSAUCE),
            (ingredient_types.INGREDIENT_TYPE_FILLING,data.NAME_FILLING_VULKAN_CUTLET, data.PRICE_VULKAN_CUTLET),
            (ingredient_types.INGREDIENT_TYPE_FILLING,data.NAME_FILLING_SALAD_MARS, data.PRICE_SALAD_MARS),
        ]
    )
    def test_get_type_should_return_correct_type_for_ingredient(self,ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type