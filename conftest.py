import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = 'test bun'
    bun.get_price.return_value = 100
    return bun


@pytest.fixture(params=["SAUCE", "FILLING"])
def ingredient(request):
    ingredient = Mock()

    ingredient.get_type.return_value = request.param
    ingredient.get_name.return_value = "test ingredient"
    ingredient.get_price.return_value = 50

    return ingredient


