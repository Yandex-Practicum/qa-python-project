import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type", ["", "SAUCE", "FILLING"])
    def test_ingredient_init_type_check(self, ingredient_type):
        ingredient = Ingredient(ingredient_type=ingredient_type, name="", price=0)
        assert ingredient.type == ingredient_type

    @pytest.mark.parametrize("ingredient_name", ["", "cutlet", "dinosaur", "sausage"])
    def test_ingredient_init_name_check(self, ingredient_name):
        ingredient = Ingredient(ingredient_type="", name=ingredient_name, price=0)
        assert ingredient.name == ingredient_name

    @pytest.mark.parametrize("ingredient_price", [100, 199.99, 300.0])
    def test_ingredient_init_price_check(self, ingredient_price):
        ingredient = Ingredient(ingredient_type="", name="", price=ingredient_price)
        assert ingredient.price == ingredient_price

    @pytest.mark.parametrize("ingredient_type", ["", "SAUCE", "FILLING"])
    def test_ingredient_get_type_check(self, ingredient_type):
        ingredient = Ingredient(ingredient_type=ingredient_type, name="", price=0)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_name", ["", "cutlet", "dinosaur", "sausage"])
    def test_ingredient_get_name_check(self, ingredient_name):
        ingredient = Ingredient(ingredient_type="", name=ingredient_name, price=0)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize("ingredient_price", [100, 199.99, 300.0])
    def test_ingredient_get_price_check(self, ingredient_price):
        ingredient = Ingredient(ingredient_type="", name="", price=ingredient_price)
        assert ingredient.get_price() == ingredient_price
