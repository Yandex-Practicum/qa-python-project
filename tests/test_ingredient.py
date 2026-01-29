class TestIngredient:

    def test_type_of_ingredient(self, ingredient):
        assert ingredient.type == 'SAUCE'

    def test_name_of_ingredient(self, ingredient):
        assert ingredient.name == 'hot sauce'

    def test_price_of_ingredient(self, ingredient):
        assert ingredient.price == 100

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 100

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == 'hot sauce'

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == 'SAUCE'