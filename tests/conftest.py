import pytest
from unittest.mock import create_autospec

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def make_bun():
    """Фабрика булок: мок строго повторяет интерфейс Bun (autospec)."""
    def _make(name="Булка", price=100.0):
        bun = create_autospec(Bun, instance=True)
        bun.get_name.return_value = name
        bun.get_price.return_value = price
        return bun
    return _make


@pytest.fixture
def make_ingredient():
    """Фабрика ингредиентов: мок строго повторяет интерфейс Ingredient."""
    def _make(type_="SAUCE", name="соус", price=10.0):
        ing = create_autospec(Ingredient, instance=True)
        ing.get_type.return_value = type_
        ing.get_name.return_value = name
        ing.get_price.return_value = price
        return ing
    return _make

