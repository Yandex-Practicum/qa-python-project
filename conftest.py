import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from data import buns, ingreds


@pytest.fixture
def bun():
    return Bun("black bun", 100)


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)


@pytest.fixture
def mock_buns_list():
    mock_buns_list = []

    mock_bun0 = Mock()
    mock_bun0.get_price.return_value = buns[0]['price']
    mock_bun0.get_name.return_value = buns[0]['name']
    mock_buns_list.append(mock_bun0)

    mock_bun1 = Mock()
    mock_bun1.get_price.return_value = buns[1]['price']
    mock_bun1.get_name.return_value = buns[1]['name']
    mock_buns_list.append(mock_bun1)

    return mock_buns_list


@pytest.fixture
def mock_ingredients_list():
    mock_ingredients_list = []

    mock_ingred0 = Mock()
    mock_ingred0.get_type.return_value = ingreds[0]['type']
    mock_ingred0.get_name.return_value = ingreds[0]['name']
    mock_ingred0.get_price.return_value = ingreds[0]['price']
    mock_ingredients_list.append(mock_ingred0)

    mock_ingred1 = Mock()
    mock_ingred1.get_type.return_value = ingreds[1]['type']
    mock_ingred1.get_name.return_value = ingreds[1]['name']
    mock_ingred1.get_price.return_value = ingreds[1]['price']
    mock_ingredients_list.append(mock_ingred1)

    return mock_ingredients_list


@pytest.fixture
def burger(mock_buns_list, mock_ingredients_list):

    burger = Burger()
    burger.bun = mock_buns_list[0]
    burger.ingredients = mock_ingredients_list

    return burger


@pytest.fixture
def database():
    return Database()
