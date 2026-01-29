import pytest
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize('ingredient_fixture, expected_type, expected_name, expected_price', [
        ('sauce', INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        ('filling', INGREDIENT_TYPE_FILLING, 'cutlet', 100)
    ])
    def test_ingredient_properties(self, request, ingredient_fixture, expected_type, expected_name, expected_price):
        ingredient = request.getfixturevalue(ingredient_fixture)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price