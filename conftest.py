import pytest

from burger import Burger
from ingredient import Ingredient
from bun import Bun


@pytest.fixture
def add_burger():
    burger = Burger()
    burger.set_buns(Bun('black bun', 10))
    burger.add_ingredient(Ingredient('vegetable', 'tomato', 5))
    burger.add_ingredient(Ingredient('dairy', 'cheese', 7))

    return burger

