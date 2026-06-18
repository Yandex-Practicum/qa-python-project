import pytest

from database import Database


@pytest.fixture
def database():
    return Database()
