import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun_mock():
    return Mock()

@pytest.fixture
def ingredient_mock():
    return Mock()