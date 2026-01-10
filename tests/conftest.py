import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger

@pytest.fixture
def bun_100():
    """Булка за 100 для тестов."""
    return Bun("black bun", 100)

@pytest.fixture
def empty_burger(bun_100):
    """Пустой бургер с булкой — используется во многих тестах."""
    b = Burger()
    b.set_buns(bun_100)
    return b

