import pytest
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()
