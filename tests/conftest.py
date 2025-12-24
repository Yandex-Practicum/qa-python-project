import pytest
from praktikum.burger import Burger
from tests.test_burger import MockBun


@pytest.fixture
def burger():
    burger = Burger()
    burger.set_buns(MockBun.mock_bun)
    return burger
