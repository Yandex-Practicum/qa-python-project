import pytest
from praktikum.praktikum import Burger
from tests.burger_test import MockBun


@pytest.fixture
def burger():
    burger = Burger()
    burger.set_buns(MockBun.mock_bun)
    return burger
