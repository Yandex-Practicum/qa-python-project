from praktikum.ingredient import Ingredient
import pytest
import data


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price', data.available_ingredients)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_price()

        assert actual_result == ingredient.price

    @pytest.mark.parametrize('ingredient_type, name, price', data.available_ingredients)
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_name()

        assert actual_result == ingredient.name

    @pytest.mark.parametrize('ingredient_type, name, price', data.available_ingredients)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_type()

        assert actual_result == ingredient.type