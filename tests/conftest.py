import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import TestData
from praktikum.database import Database


@pytest.fixture(params=[
    ('Baguette 123', 100.99),
    ('Бриошь', 150)
])
def bun(request):
    name, price = request.param
    return Bun(name, price)


@pytest.fixture
def ingredient():
    return Ingredient(TestData.ingredient_type, TestData.ingredient_name, TestData.ingredient_price)


@pytest.fixture
def database():
    return Database()