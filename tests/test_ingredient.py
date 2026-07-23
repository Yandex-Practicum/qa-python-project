import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type", ["SAUCE", "FILLING"])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "some name", 0)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"])
    def test_get_name(self, name):
        ingredient = Ingredient("SAUCE", name, 0)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [100, 200, 300])
    def test_get_price(self, price):
        ingredient = Ingredient("SAUCE", "some name", price)
        assert ingredient.get_price() == price

class TestIngredientNegative:

    @pytest.mark.parametrize("ingredient_type", ["", "UNKNOWN"])
    def test_ingredient_negative_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "some name", 100)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["", None])
    def test_ingredient_negative_name(self, name):
        ingredient = Ingredient("SAUCE", name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [-50, 0])
    def test_ingredient_negative_price(self, price):
        ingredient = Ingredient("SAUCE", "some name", price)
        assert ingredient.get_price() == price
