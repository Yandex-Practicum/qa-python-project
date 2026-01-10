import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type', ['начинка', 'соус'])
    def test_get_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'название', 12.3)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_name', ['Чесночный', 'Котлета', '123'])
    def test_get_ingredient_name(self, ingredient_name):
        ingredient = Ingredient('тип_ингредиента', ingredient_name, 123.45)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('ingredient_price', [0, -1, 1, 1.0, 123.45])
    def test_get_ingredient_price(self, ingredient_price):
        ingredient = Ingredient('тип_ингредиента', 'название_ингредиента', ingredient_price)
        assert ingredient.get_price() == ingredient_price
