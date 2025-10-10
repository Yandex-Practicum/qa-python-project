import data


class TestIngredient:

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == data.PRICE_INGREDIENT

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == data.NAME_INGREDIENT

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == data.TYPE_INGREDIENT