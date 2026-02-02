import pytest
from praktikum.database import Database
from unittest.mock import Mock


@pytest.fixture
def db():
    return Database()


@pytest.fixture
def mock_bun():
    return Mock()


@pytest.fixture
def mock_ingredient():
    return Mock()
