import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient



class TestIngredient:

    def test_get_price_OK(self, mock_ingredient):
        assert mock_ingredient.get_price() == 100

    def test_get_name_OK(self, mock_ingredient):
        assert mock_ingredient.get_name() == 'hot sauce'


    @pytest.mark.parametrize("ingredient_type", [
        [('sauce')],
        [('filling')]
    ])

    def test_get_type_OK(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'hot sauce', 100)
        assert ingredient.get_type() == ingredient_type
