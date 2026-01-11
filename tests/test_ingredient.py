from data import Data


class TestIngredient:
    def test_get_price_return_true_value(self, ingredient):
        price = ingredient.get_price()
        assert price == Data.ingredient[2]

    def test_get_name_return_true_value(self, ingredient):
        name = ingredient.get_name()
        assert name == Data.ingredient[1]

    def test_get_type_return_true_value(self, ingredient):
        value = ingredient.get_type()
        assert value == Data.ingredient[0]

