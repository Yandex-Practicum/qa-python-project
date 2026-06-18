class TestIngredient:

    def test_getting_price(self, ingredient):
        assert ingredient.get_price() == 70.0

    def test_getting_name(self, ingredient):
        assert ingredient.get_name() == 'cheese'

    def test_getting_type(self, ingredient):
        assert ingredient.get_type() == 'FILLING'
