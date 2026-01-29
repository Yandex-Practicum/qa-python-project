import pytest
from ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize(
        'type_ingredient, name, price',
        [
            ('sauce', 'ketchup', 5),
            ('sauce', 'ketchup', -5),
            ('sauce', 'ketchup', '5'),
            ('sauce', 'ketchup', 5.25)
        ]
    )
    def test_get_price(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_price() == price


    @pytest.mark.parametrize(
        'type_ingredient, name, price',
        [
            ('sauce', 'ketchup', 5),
            ('sauce', '', 5),
            ('sauce', 0, 5),
            ('sauce', None, 5)
        ]
    )
    def test_get_name(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_name() == name


    @pytest.mark.parametrize(
        'type_ingredient, name, price',
        [
            ('sauce', 'ketchup', 5),
            ('', 'ketchup', 5),
            (1.0, 'ketchup', 5),
            (None, 'ketchup', 5)
        ]
    )
    def test_get_type(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        assert ingredient.get_type() == type_ingredient
