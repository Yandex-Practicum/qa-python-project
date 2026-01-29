import pytest
from praktikum.burger import Burger


@pytest.fixture
def burgers():
    burgers = Burger()
    return burgers

