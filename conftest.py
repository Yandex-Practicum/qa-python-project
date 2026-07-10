import pytest

from burger import Burger
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE
from ingredient import Ingredient
from bun import Bun



@pytest.fixture(scope="function")
def bun():
    return Bun("Белая булка", 100)

@pytest.fixture(scope="function")
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Сыр", 50)

@pytest.fixture(scope="function")
def burger():
    return Burger()

@pytest.fixture(scope="function")
def database():
    return Database()