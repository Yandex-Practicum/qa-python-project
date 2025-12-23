import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100)
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize('ingredient_type,name,price,expected_type', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100, INGREDIENT_TYPE_FILLING)
    ])
    def test_get_type(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize('ingredient_type,name,price,expected_name', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100, 'hot sauce'),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100, 'cutlet')
    ])
    def test_get_name(self, ingredient_type, name, price, expected_name):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize('ingredient_type,name,price,expected_price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100, 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100, 100)
    ])
    def test_get_price(self, ingredient_type, name, price, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_price

