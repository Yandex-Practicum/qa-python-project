import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize("name", ["чесночный", "кетчуп", ""])
    def test_return_correct_name_when_ingredient_is_created(self, name):
        ingredient = Ingredient("соус", name, 1.0)

        assert ingredient.get_name() == name
        assert ingredient.name == name

    @pytest.mark.parametrize("curr_type", ["соус", "начинка", ""])
    def test_return_correct_type_when_ingredient_is_created(self, curr_type):
        ingredient = Ingredient(curr_type, "fake_ingredient", 1.5)

        assert ingredient.get_type() == curr_type
        assert ingredient.type == curr_type

    @pytest.mark.parametrize("price", [5, -5, 0.0, 1.5])
    def test_return_correct_price_when_ingredient_is_created(self, price):
        ingredient = Ingredient("fake_type", "fake_ingredient", price)

        assert ingredient.get_price() == price
        assert ingredient.price == price
