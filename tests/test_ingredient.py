import pytest
from source_code.ingredient import Ingredient
from data.data import ORDER_DATA_CORRECT


class TestIngredient:

    @pytest.mark.parametrize("order_data", ORDER_DATA_CORRECT)
    def test_ingredient_name(self, order_data):
        ingredient = Ingredient(order_data["ingredient_type"], order_data["ingredient_name"], order_data["ingredient_price"])
        assert ingredient.get_name() == order_data["ingredient_name"] and isinstance(order_data["ingredient_name"], str)

    @pytest.mark.parametrize("order_data", ORDER_DATA_CORRECT)
    def test_ingredient_type(self, order_data):
        ingredient = Ingredient(order_data["ingredient_type"], order_data["ingredient_name"], order_data["ingredient_price"])
        assert ingredient.get_type() == order_data["ingredient_type"] and isinstance(order_data["ingredient_type"], str)

    @pytest.mark.parametrize("order_data", ORDER_DATA_CORRECT)
    def test_ingredient_price(self, order_data):
        ingredient = Ingredient(order_data["ingredient_type"], order_data["ingredient_name"], order_data["ingredient_price"])
        assert ingredient.get_price() == order_data["ingredient_price"] and isinstance(order_data["ingredient_price"], float)
