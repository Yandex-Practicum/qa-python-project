import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.burger import Burger

@pytest.fixture
def bun():
    return Bun('Флюоресцентная булка R2-D3', 988)

@pytest.fixture
def database():
    return Database()

@pytest.fixture()
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)

@pytest.fixture()
def burger():
    return Burger()