import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:
    list_data_types = ["SAUCE", "FILLING"]
    list_data_names = ["hot sauce", "cutlet", "", "1", "c" * 100]
    list_data_price = [100.0, 200.0, 0.0, 0.01, 999.99]

    @pytest.mark.parametrize("types", list_data_types)
    def test_ingredients_types(self, types):
        name = "hot sauce"
        price = 100.0
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_type() == types

    @pytest.mark.parametrize("name", list_data_names)
    def test_ingredients_names(self, name):
        types = "SAUCE"
        price = 100.0
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", list_data_price)
    def test_ingredients_price(self, price):
        types = "SAUCE"
        name = "hot sauce"
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_price() == price
