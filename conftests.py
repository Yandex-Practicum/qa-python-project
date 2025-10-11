import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING

@pytest.fixture

def bun_mock():
    bun_mock = Mock()
    bun_mock.name = "Булка"
    bun_mock.price = 10.00
    bun_mock.get_name.return_value = bun_mock.name
    bun_mock.get_price.return_value = 10.00
    return bun_mock

@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.name = "Котлета"
    ingredient_mock.price = 30.00
    ingredient_mock.type = FILLING
    ingredient_mock.get_name.return_value = ingredient_mock.name
    ingredient_mock.get_type.return_value = ingredient_mock.type
    ingredient_mock.get_price.return_value = 30.00
    return ingredient_mock

@pytest.fixture
def sauce_mock():
    sauce_mock = Mock()
    sauce_mock.name = "Соус"
    sauce_mock.price = 20.00
    sauce_mock.type = SAUCE
    sauce_mock.get_name.return_value = sauce_mock.name
    sauce_mock.get_type.return_value = sauce_mock.type
    sauce_mock.get_price.return_value = 20.00
    return sauce_mock
