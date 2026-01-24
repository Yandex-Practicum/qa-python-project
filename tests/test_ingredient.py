class TestIngredient:

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == ingredient.price

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == ingredient.name

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == ingredient.type
