import pytest
from praktikum.ingredient import Ingredient
from data_for_tests.data_ingrid import DataIngrid


class TestForIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", DataIngrid.all_ingrids)
    def test_ingrid_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", DataIngrid.all_ingrids)
    def test_ingrid_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", DataIngrid.all_ingrids)
    def test_ingrid_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
