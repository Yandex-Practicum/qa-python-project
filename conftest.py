import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import TestData


# Фикстура для создания экземпляра класса Burger
@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = TestData.buns[1][0]
    bun.get_price.return_value = TestData.buns[1][1]
    return bun


@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = TestData.ingredients[0][1]
    ingredient.get_price.return_value = TestData.ingredients[0][2]
    return ingredient


@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = TestData.ingredients[9][1]
    ingredient.get_price.return_value = TestData.ingredients[9][2]
    return ingredient


# Фикстура для создания экземпляра класса Database
@pytest.fixture
def database():
    return Database()
