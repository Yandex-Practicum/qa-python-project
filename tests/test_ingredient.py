import pytest
from data import DataIngredient
from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize(
        "type_ingredient",
        [
            ingredient_types.INGREDIENT_TYPE_FILLING,
            ingredient_types.INGREDIENT_TYPE_SAUCE,
        ]
    )
    def test_get_type_ingredient_received(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, DataIngredient.NAME_SAUCE, DataIngredient.PRICE_SAUCE)

        assert ingredient.get_type() == type_ingredient

    def test_get_price_received(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, DataIngredient.NAME_SAUCE,
                                DataIngredient.PRICE_SAUCE)

        assert ingredient.get_price() == DataIngredient.PRICE_SAUCE

    def test_get_name_received(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, DataIngredient.NAME_FILLING,
                                DataIngredient.NAME_FILLING)

        assert ingredient.get_name() == DataIngredient.NAME_FILLING
