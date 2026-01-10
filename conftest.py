import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.burger import Burger

@pytest.fixture
def bun():
    return Bun("black bun", 100)

@pytest.fixture
def ingredient():
    return Ingredient("SAUCE", "hot sauce", 50)