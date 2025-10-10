import pytest
from unittest.mock import Mock

from praktikum.database import Database
from praktikum.burger import Burger


@pytest.fixture
def sample_burger():
    bun = Mock()
    bun.get_name.return_value = "Краторная булка"
    bun.get_price.return_value = 100

    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "Соус традиционный"
    sauce.get_price.return_value = 50

    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "Говяжий метеорит"
    filling.get_price.return_value = 3000

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    return burger


@pytest.fixture
def empty_burger():
    return Burger()


@pytest.fixture(scope="class")
def db():
    return Database()