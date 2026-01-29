import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from unittest.mock import create_autospec


@pytest.fixture
def bun():
    return Bun(name='Краторная булка', price=1255.0)

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    return create_autospec(Bun)

@pytest.fixture
def mock_ingredient():
    return create_autospec(Ingredient)

@pytest.fixture
def ingredient():
    return Ingredient('FILLING', 'Говяжий метеорит (отбивная)', 3000.0)

@pytest.fixture
def database():
    return Database()
