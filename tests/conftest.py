import pytest
from praktikum.burger import Burger


@pytest.fixture
def burger():
    """Перед каждым тестом создаётся новый экземпляр Burger, чтобы тесты не влияли друг на друга"""
    return Burger()
