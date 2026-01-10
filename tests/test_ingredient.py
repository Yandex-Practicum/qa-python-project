import pytest
from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'barbecue', 10],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'tomatoes', 15]
    ])
    def test_get_price_valid_price_returned_correct_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_price()
        assert actual_result == price

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'garlic', 8.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'bacon', 25]
    ])
    def test_get_name_valid_name_returned_correct_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_name()
        assert actual_result == name

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'cheese', 6.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'pickles', 12.5]
    ])
    def test_get_type_valid_type_returned_correct_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_type()
        assert actual_result == ingredient_type
