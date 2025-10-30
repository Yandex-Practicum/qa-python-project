import pytest
from praktikum.bun import Bun
from data import data
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from typing import List

#Создаем объект булочки
@pytest.fixture
def bun():
    name = data.bun_name
    price = data.bun_price
    bun = Bun(name, price)
    return bun

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def ingredient():
    ingredient_type = data.ingredient_type
    ingredient_name = data.ingredient_name
    ingredient_price = data.ingredient_price
    ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
    return ingredient

@pytest.fixture
def database():
    database = Database()
    return database
