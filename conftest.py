import pytest
from praktikum.burger import Burger


@pytest.fixture
def burger():
    """Каждый тест получает новый, чистый Burger."""
    return Burger()
