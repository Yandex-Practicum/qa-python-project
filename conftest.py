import pytest
from praktikum.bun import Bun
from data import data
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database


@pytest.fixture
def bun_data():
    return {"name": data.bun_name, "price": data.bun_price}


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def ingredient_data():
    return {
        "type": data.ingredient_type,
        "name": data.ingredient_name,
        "price": data.ingredient_price
    }


@pytest.fixture
def database():
    database = Database()
    return database