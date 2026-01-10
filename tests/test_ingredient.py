from praktikum.ingredient import Ingredient
import pytest

class TestIngredient:
    @pytest.mark.parametrize('type, name, price',
                             [['sauce', 'hot', 10],
                              ['filling', 'meat', 200]])
    def test_get_price(self, type, name, price):

        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('type, name, price',
                             [ ['sauce', 'hot', 10],
                               ['filling', 'meat', 200] ])
    def test_get_name(self, type, name, price):

        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('type, name, price',
                             [['sauce', 'hot', 10],
                              ['filling', 'meat', 200]])
    def test_get_type(self, type, name, price):

        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type