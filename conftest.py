import pytest

from unittest.mock import Mock
from data import TestData
from practicum.burger import Burger


@pytest.fixture(params=TestData.buns)
def bun_data(request):
    bun = Mock()
    bun.get_name.return_value = request.param[0]
    bun.get_price.return_value = request.param[1]
    return bun

@pytest.fixture
def mock_ingredient():
    def _create(ingredient_type, ingredient_name, ingredient_price):
        test_ingredient = Mock()
        test_ingredient.get_type.return_value = ingredient_type
        test_ingredient.get_name.return_value = ingredient_name
        test_ingredient.get_price.return_value = ingredient_price
        return test_ingredient
    return _create

@pytest.fixture
def burger_with_bun(bun_data):
    burger = Burger()
    burger.set_buns(bun_data)
    return burger
