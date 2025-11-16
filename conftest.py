from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture(params=[
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def bun(request):
    name, price = request.param
    return Bun(name,price)

@pytest.fixture(params=[
    ('Соус','Соус Spicy-X', 90),
    ('Начинки','Мясо бессмертных моллюсков', 1337),
])
def ingredient(request):
    ingredient, name, price = request.param
    return Ingredient(ingredient, name, price)

@pytest.fixture
def database():
    return Database()


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = None
    mock_bun.price = None
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = None
    mock_ingredient.name = None
    mock_ingredient.price = None
    return mock_ingredient
