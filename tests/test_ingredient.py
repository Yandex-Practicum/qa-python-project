from data import TestData


class TestIngredient:

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == TestData.ingredient_price

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == TestData.ingredient_name

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == TestData.ingredient_type





