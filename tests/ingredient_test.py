from conftest import ingredient
from data import ingredient1_test


class TestIngredient:
    def test_get_type(self, ingredient):
        assert ingredient.get_type() == ingredient1_test["type"]

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == ingredient1_test["name"]

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == ingredient1_test["price"]
