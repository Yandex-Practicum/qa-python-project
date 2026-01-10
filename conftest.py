import pytest

from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture(scope="module")
def database():
    return Database()


@pytest.fixture
def burger():
    return Burger()
