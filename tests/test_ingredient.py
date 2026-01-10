import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('price', [
        100, 46.88, 0
    ])
    def test_get_price_returned_added_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('price', [
        100, 46.88, 0
    ])
    def test_price_type_is_number(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', price)
        assert isinstance(ingredient.get_price(), (int, float))

    def test_get_name_returned_added_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert ingredient.get_name() == 'hot sauce'

    def test_name_type_is_str(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert isinstance(ingredient.get_name(), str)

    @pytest.mark.parametrize('ingredient_type', [
        INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
    ])
    def test_get_type_returned_added_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'hot sauce', 100)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type', [
        INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
    ])
    def test_ingredient_type_is_str(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'hot sauce', 100)
        assert isinstance(ingredient.get_type(), str)
