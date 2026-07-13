from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def black_bun():
    return Bun("black bun", 100)


@pytest.fixture
def bun(request):
    name, price = request.param
    return Bun(name, price)


@pytest.fixture
def ingredient(request):
    ingredient_type, name, price = request.param
    return Ingredient(ingredient_type, name, price)


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredient_mock():
    ingredient = Mock()
    ingredient.get_name.return_value = "ketchup"
    ingredient.get_price.return_value = 50
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient


@pytest.fixture
def second_ingredient_mock():
    return Mock()


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def burger_with_bun(burger, bun_mock):
    burger.set_buns(bun_mock)
    return burger


@pytest.fixture
def burger_with_one_ingredient(burger_with_bun, ingredient_mock):
    burger_with_bun.add_ingredient(ingredient_mock)
    return burger_with_bun


@pytest.fixture
def burger_with_two_ingredients(burger_with_bun, ingredient_mock, second_ingredient_mock):
    burger_with_bun.add_ingredient(ingredient_mock)
    burger_with_bun.add_ingredient(second_ingredient_mock)
    return burger_with_bun


@pytest.fixture
def burger_for_price(bun_mock, request):
    burger = Burger()
    burger.set_buns(bun_mock)
    for price in request.param:
        ingredient = Mock()
        ingredient.get_price.return_value = price
        burger.add_ingredient(ingredient)
    return burger


@pytest.fixture
def database():
    return Database()
