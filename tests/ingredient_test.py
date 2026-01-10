from praktikum.ingredient_types import *


class TestIngredient:
    def test_get_price_true(self, ingredient):
        assert ingredient.get_price() == 555

    def test_get_name_true(self, ingredient):
        assert ingredient.get_name() == 'crazy sauce'

    def test_get_type_true(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
