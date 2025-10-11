import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger


@pytest.fixture()
def bun_mock():
    bun_mock = MagicMock()
    bun_mock.get_name.return_value = 'black bun'
    bun_mock.get_price.return_value = 100.50
    return bun_mock


@pytest.fixture()
def ingredient_mock():
    ingredient_mock = MagicMock()
    ingredient_mock.get_price.return_value = 250.50
    ingredient_mock.get_name.return_value = 'sour cream'
    ingredient_mock.get_type.return_value = 'FILLING'
    return ingredient_mock

@pytest.fixture()
def another_ingredient_mock():
    ingredient_mock = MagicMock()
    ingredient_mock.get_price.return_value = 155.78
    ingredient_mock.get_name.return_value = 'cutlet'
    ingredient_mock.get_type.return_value = 'FILLING'
    return ingredient_mock
@pytest.fixture()
def burger():
    return Burger()
