import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "Урановая булка"
    bun_mock.get_price.return_value = 50.0
    return bun_mock

@pytest.fixture
def ingredient_sauce():
    sauce_mock = Mock()
    sauce_mock.get_name.return_value = "Святящаяся горчица"
    sauce_mock.get_type.return_value = "SAUCE"
    sauce_mock.get_price.return_value = 10.0
    return sauce_mock

@pytest.fixture
def ingredient_filling():
    filling_mock = Mock()
    filling_mock.get_name.return_value = "Лук с планеты Плюк"
    filling_mock.get_type.return_value = "FILLING"
    filling_mock.get_price.return_value = 100.0
    return filling_mock