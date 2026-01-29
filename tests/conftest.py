import pytest

import data
from praktikum.bun import Bun
from praktikum.burger import Burger


@pytest.fixture
def fixt_set_bun():
    return Bun("test_bun", 10)


@pytest.fixture()
def fixt_set_burger(fixt_set_bun):
    burger = Burger()
    burger.set_buns(fixt_set_bun)
    for test_ingredient in data.generator_ingredients(3):
        burger.add_ingredient(test_ingredient)
    return burger
