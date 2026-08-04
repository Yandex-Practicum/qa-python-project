import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger_with_data():
    burger = Burger()
    bun = Bun("black bun", 100)
    ingredient1 = Ingredient("SAUCE", "hot sauce", 50)
    ingredient2 = Ingredient("FILLING", "cutlet", 150)
    return burger, bun, ingredient1, ingredient2
