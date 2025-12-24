import pytest
from praktikum.bun import Bun
from unittest.mock import Mock
import data
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


@pytest.fixture()
def create_bun():
    bun = Bun(data.BUN_NAME, data.BUN_PRICE)
    return bun


@pytest.fixture()
def create_ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, data.INGREDIENT_NAME_SAUCE, data.INGREDIENT_PRICE_SAUCE)
    return ingredient


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = data.BUN_NAME
    mock_bun.price = data.BUN_PRICE
    mock_bun.get_name.return_value = data.BUN_NAME
    mock_bun.get_price.return_value = data.BUN_PRICE
    return mock_bun


@pytest.fixture()
def mock_ingredient_sauce():
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.name = data.INGREDIENT_NAME_SAUCE
    mock_ingredient_sauce.price = data.INGREDIENT_PRICE_SAUCE
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.get_name.return_value = data.INGREDIENT_NAME_SAUCE
    mock_ingredient_sauce.get_price.return_value = data.INGREDIENT_PRICE_SAUCE
    return mock_ingredient_sauce


@pytest.fixture()
def mock_ingredient_filling():
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.type = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.name = data.INGREDIENT_NAME_FILLING
    mock_ingredient_filling.price = data.INGREDIENT_PRICE_FILLING
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.get_name.return_value = data.INGREDIENT_NAME_FILLING
    mock_ingredient_filling.get_price.return_value = data.INGREDIENT_PRICE_FILLING
    return mock_ingredient_filling


@pytest.fixture()
def burger(mock_ingredient_sauce, mock_ingredient_filling):
    burger = Burger()
    burger.ingredients.append(mock_ingredient_filling)
    burger.ingredients.append(mock_ingredient_sauce)
    return burger
