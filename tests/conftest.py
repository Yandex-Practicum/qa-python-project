# покрываемый unit-тестами класс
from praktikum.burger import Burger
# фреймворк системы тестирования
import pytest


@pytest.fixture
def burger():
    burger = Burger()
    return burger
