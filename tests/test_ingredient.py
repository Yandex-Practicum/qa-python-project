from data import ingredient_name, ingredient_price, ingredient_type


class TestIngredient:
    def test_get_price(self, ingredient):
        assert ingredient.get_price() == ingredient_price

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == ingredient_name

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == ingredient_type
