import pytest
from data import ingreds


class TestIngredient:

    @pytest.mark.parametrize('ingredient_data', ingreds)
    def test_get_price(self, ingredient, ingredient_data):
        ingredient.price = ingredient_data['price']

        assert ingredient.get_price() == ingredient.price

    @pytest.mark.parametrize('ingredient_data', ingreds)
    def test_get_name(self, ingredient, ingredient_data):
        ingredient.name = ingredient_data['name']

        assert ingredient.get_name() == ingredient.name

    @pytest.mark.parametrize('ingredient_data', ingreds)
    def test_get_type(self, ingredient, ingredient_data):
        ingredient.type = ingredient_data['type']

        assert ingredient.get_type() == ingredient.type
