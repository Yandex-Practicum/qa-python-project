import pytest

from DATA import Buns, Price, Ingridients
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def mock_bun():
    return Bun(Buns.WHITE_BUN, Price.WHITE_BUN_PRICE)


@pytest.fixture
def mock_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, Ingridients.HOT_SAUCE, Price.HOT_SAUCE)


@pytest.fixture
def mock_ingredient_2():
    return Ingredient(INGREDIENT_TYPE_SAUCE, Ingridients.HOT_SAUCE, Price.HOT_SAUCE)


@pytest.fixture
def burger_complete(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger


@pytest.fixture
def db():
    db = Database()
    return db
