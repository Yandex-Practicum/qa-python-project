import pytest

from praktikum.burger import Burger
from praktikum.database import Database

from data.burger_data import MockData


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture()
def db():
    db = Database()
    return db


@pytest.fixture
def burger_with_mock_ingredients():
    burger = Burger()
    burger.set_buns(MockData.mock_bun)
    burger.add_ingredient(MockData.mock_ingredient_1)
    burger.add_ingredient(MockData.mock_ingredient_1)
    burger.add_ingredient(MockData.mock_ingredient_2)
    return burger
