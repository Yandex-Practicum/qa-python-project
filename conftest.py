import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database



@pytest.fixture(scope = 'function')
def bun():
    return Bun('white bun', 100)

@pytest.fixture(scope = 'function')
def burger():
    return Burger()

@pytest.fixture(scope = 'function')
def db():
    return Database()