import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def database():
    database = Database()
    return database

@pytest.fixture
def bun_mock():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = 'test bun'
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def ingredient_mock():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = 'test ingredient'
    ingredient.get_price.return_value = 100
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient