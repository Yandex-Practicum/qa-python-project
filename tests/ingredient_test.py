from data import test_data
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_name(self, ingredient):
       assert ingredient.get_name() == test_data.INGREDIENT_NAME

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == test_data.INGREDIENT_PRICE

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
