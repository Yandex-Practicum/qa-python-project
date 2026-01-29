import pytest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun_mock():
    mock = Mock()
    mock.get_name.return_value = 'Bun'
    mock.get_price.return_value = 100
    return mock

@pytest.fixture
def cheese_mock():
    mock = Mock()
    mock.get_name.return_value = 'Cheese'
    mock.get_price.return_value = 50
    mock.get_type.return_value = 'sauce'
    return mock

@pytest.fixture
def tomato_mock():
    mock = Mock()
    mock.get_name.return_value = 'Tomato'
    mock.get_price.return_value = 75
    mock.get_type.return_value = 'filling'
    return mock
