from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

from data import Data


class TestBun:

    @classmethod
    def setup_class(cls):
        cls.buns = Ingredient(INGREDIENT_TYPE_SAUCE, Data.ING_NAME, Data.ING_PRICE)

    def test_get_ingredient_name(self):
        result = self.buns.get_name()
        assert Data.ING_NAME == result, 'The answer does not match the expected result'

    def test_get_ingredient_price(self):
        result = self.buns.get_price()
        assert Data.ING_PRICE == result, 'The answer does not match the expected result'

    def test_get_ingredient_type(self):
        result = self.buns.get_type()
        assert INGREDIENT_TYPE_SAUCE == result, 'The answer does not match the expected result'
