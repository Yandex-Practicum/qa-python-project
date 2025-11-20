import pytest

from praktikum.burger import Burger

@pytest.fixture
def burger():
    burger = Burger()
    return burger

