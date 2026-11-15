import pytest
import data
import ingredient
import ingredient_types

class TestingIngredient:

    @pytest.mark.parametrize("type_ing, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_int),
        (ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_float)
    ])
    def test_get_price_success(self, type_ing, name, price):
        test_ingredient = ingredient.Ingredient(type_ing, name, price)
        assert test_ingredient.get_price() == price

    @pytest.mark.parametrize("type_ing, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_int),
        (ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_float)
    ])
    def test_get_name_success(self, type_ing, name, price):
        test_ingredient = ingredient.Ingredient(type_ing, name, price)
        assert test_ingredient.get_name() == name

    @pytest.mark.parametrize("type_ing, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_int),
        (ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_float)
    ])
    def test_get_type_success(self, type_ing, name, price):
        test_ingredient = ingredient.Ingredient(type_ing, name, price)
        assert test_ingredient.get_type() == type_ing
