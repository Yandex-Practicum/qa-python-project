import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

@pytest.fixture
def bun():
    return Bun("Булка звездной пыли", 100)

@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, "Кольца j1407b", 280)

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()