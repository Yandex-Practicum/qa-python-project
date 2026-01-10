#Ingredients Class tests
from data import INGREDIENT
from conftest import test_ingredient, test_ingredient2
import pytest


class TestIngredient:

    def test_init_ingredient_type_matches(self, test_ingredient):
        assert (isinstance(test_ingredient.type, str) and test_ingredient.type == INGREDIENT['ingredient_type'])

    def test_init_ingredient_name_matches(self, test_ingredient):
        assert isinstance(test_ingredient.name, str) and test_ingredient.name == INGREDIENT['name']

    @pytest.mark.parametrize('test_ingredient', [test_ingredient, test_ingredient2],
                             indirect=True)  # check int and float price values
    def test_init_ingredient_price_matches(self, test_ingredient):
        assert isinstance(test_ingredient.price, (int, float)) and test_ingredient.price == INGREDIENT['price']

    def test_get_name_returns_correct_name(self, test_ingredient):
        assert isinstance(test_ingredient.get_name(), str) and test_ingredient.get_name() == INGREDIENT['name']

    @pytest.mark.parametrize('test_ingredient', [test_ingredient, test_ingredient2],
                             indirect=True)  # check int and float price values
    def test_get_price_returns_correct_price(self, test_ingredient):
        assert (
                isinstance(test_ingredient.get_price(), (int, float)) and
                test_ingredient.get_price() == INGREDIENT['price']
        )

    def test_get_type_returns_correct_type(self, test_ingredient):
        _type = test_ingredient.get_type()
        assert (
                isinstance(test_ingredient.get_type(), str) and
                test_ingredient.get_type() == INGREDIENT['ingredient_type']
        )
