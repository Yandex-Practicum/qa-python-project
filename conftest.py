from praktikum.burger import Burger
from praktikum.bun import Bun
from data import bun_data
import pytest

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun(**bun_data)