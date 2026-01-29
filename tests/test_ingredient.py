from data import Data
from praktikum.ingredient import *
from praktikum.ingredient_types import *


class TestIngredient:
    def test_get_name_of_bun_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.ingredient_type_sauce,
                                Data.ingredient_price_sauce)
        assert ingredient.get_name() == 'Chili sauce'

    def test_get_price_of_bun_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.ingredient_type_sauce,
                                Data.ingredient_price_sauce)
        assert ingredient.get_price() == 300.0

    def test_get_type_of_bun_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.ingredient_type_sauce,
                                Data.ingredient_price_sauce)
        assert ingredient.get_type() == 'SAUCE'
