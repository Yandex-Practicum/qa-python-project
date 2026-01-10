import pytest
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def db():
    return Database()

@pytest.fixture
def burger():
    return Burger()
