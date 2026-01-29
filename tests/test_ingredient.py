from tests.data import MockIngredient


class TestIngredient:

    def test_get_name_return_name(self, mok_ingredient):
        assert mok_ingredient.get_name() == MockIngredient.NAME

    def test_get_price_return_price(self, mok_ingredient):
        assert mok_ingredient.get_price() == MockIngredient.PRICE

    def test_get_type_return_type(self, mok_ingredient):
        assert mok_ingredient.get_type() == MockIngredient.TYPE
