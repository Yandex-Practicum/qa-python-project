from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


# фикстура булочки
@pytest.fixture(scope="function")
def bun():
    bun = Bun('bun', 50)

    return bun


# фикстура ингредиента (соуса)
@pytest.fixture(scope="function")
def ingredient():
    ingredient = Ingredient('sauce', 'spicy', 20)

    return ingredient


# фикстура бургера
@pytest.fixture(scope="function")
def burger():
    burger = Burger()

    return burger


# фикстура датабазы
@pytest.fixture(scope="function")
def database():
    database = Database()

    return database


# фикстура мока булочки
@pytest.fixture(scope="function")
def mock_bun():
    bun = Mock()
    bun.name = 'bun_mock'
    bun.price = 100
    bun.get_name.return_value = 'bun_mock'
    bun.get_price.return_value = 100

    return bun


# фикстура мока ингредиента (соуса)
@pytest.fixture(scope="function")
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.type = 'sauce_mock'
    ingredient.name = 'ketchup'
    ingredient.price = 10
    ingredient.get_type.return_value = 'sauce_mock'
    ingredient.get_name.return_value = 'ketchup'
    ingredient.get_price.return_value = 10

    return ingredient


# фикстура мока ингредиента (начинки)
@pytest.fixture(scope="function")
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.type = 'filling_mock'
    ingredient.name = 'meat'
    ingredient.price = 30
    ingredient.get_type.return_value = 'filling_mock'
    ingredient.get_name.return_value = 'meat'
    ingredient.get_price.return_value = 30

    return ingredient
