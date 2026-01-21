from data import Data


class TestIngredient:

    def test_get_name(self, new_ingredient):
        assert new_ingredient.get_name() == Data.INGREDIENT_NAME

    def test_get_price(self, new_ingredient):
        assert new_ingredient.get_price() == Data.INGREDIENT_PRICE

    def test_get_type(self, new_ingredient):
        assert new_ingredient.get_type() == Data.INGREDIENT_TYPE
