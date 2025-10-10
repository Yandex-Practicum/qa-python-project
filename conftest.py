import pytest
from typing import List

from unittest.mock import Mock, patch

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

from praktikum.ingredient_types import *
from data import Data


# фикстура для создания объекта класса Burger
@pytest.fixture()
def burger():
    return Burger()


# фикстура для заполнения базы данных моками булок и ингридиентов
@patch('praktikum.database.Bun')
@patch('praktikum.database.Ingredient')
@pytest.fixture()
def put_buns_and_ingredients_into_database(bun_mock, ingredient_sauce_mock, ingredient_filling_mock):
    db = Database()
    db.buns = []
    db.ingredients = []

    db.buns.append(Bun("black bun", 100))
    db.buns.append(Bun("white bun", 200))
    db.buns.append(Bun("red bun", 300))

    db.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
    db.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200))
    db.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300))

    db.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
    db.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200))
    db.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))
    return db


# фикстура - мок для булки
@pytest.fixture()
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = "red bun"
    mock_bun.price = 100
    return mock_bun


# фикстура - мок для соуса
@pytest.fixture()
def ingredient_sauce_mock():
    mock_ingredient = Mock()
    mock_ingredient.ingredient_type = INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = "hot sauce"
    mock_ingredient.price = 100
    return mock_ingredient


# фикстура - мок для начинки
@pytest.fixture()
def ingredient_filling_mock():
    mock_ingredient = Mock()
    mock_ingredient.ingredient_type = INGREDIENT_TYPE_FILLING
    mock_ingredient.name = "sausage"
    mock_ingredient.price = 300
    return mock_ingredient


# фикстура на создание бургера со стоимостью компонентов
@pytest.fixture()
def get_price_burger_components(request, burger, bun_mock, ingredient_sauce_mock, ingredient_filling_mock):
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_sauce_mock)
    burger.add_ingredient(ingredient_filling_mock)
    bun_mock.get_name.return_value = request.param["bun_name"]
    ingredient_sauce_mock.get_name.return_value = request.param["sauce_name"]
    ingredient_filling_mock.get_name.return_value = request.param["filling_name"]
    ingredient_sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient_filling_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    bun_mock.get_price.return_value = request.param["bun_price"]
    ingredient_sauce_mock.get_price.return_value = request.param["sauce_price"]
    ingredient_filling_mock.get_price.return_value = request.param["filling_price"]
    return burger
