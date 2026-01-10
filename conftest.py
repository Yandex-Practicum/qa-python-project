import pytest
from praktikum.database import Database


@pytest.fixture()
def init_database():
    return Database()