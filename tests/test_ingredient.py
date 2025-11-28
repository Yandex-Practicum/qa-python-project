import pytest
from praktikum.ingredient import Ingredient
from data.ingredient_data import get_ingredient_test_data


class TestIngredient:

    def test_ingredient_creation_attributes(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        assert ingredient.type == "SAUCE"
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100

    def test_get_price_returns_correct_price(self):
        ingredient = Ingredient("FILLING", "cutlet", 200)
        assert ingredient.get_price() == 200

    def test_get_name_returns_correct_name(self):
        ingredient = Ingredient("SAUCE", "sour cream", 150)
        assert ingredient.get_name() == "sour cream"

    def test_get_type_returns_correct_type(self):
        ingredient = Ingredient("FILLING", "dinosaur", 300)
        assert ingredient.get_type() == "FILLING"

    @pytest.mark.parametrize("ingredient_type,name,price", get_ingredient_test_data())
    def test_ingredient_creation_with_different_parameters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
