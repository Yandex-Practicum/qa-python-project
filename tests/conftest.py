from unittest.mock import Mock

import pytest
from bun import Bun
from ingredient import Ingredient
from burger import Burger
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BunData, IngredientSauceData, IngredientFillingData


@pytest.fixture (params=BunData.data, scope='function')
def default_bun(request):
    bun_name, bun_price = request.param
    bun = Bun(bun_name, bun_price)
    return bun

@pytest.fixture (params=IngredientSauceData.data, scope='function')
def ingredient_sauce(request):
    sauce_name, sauce_price = request.param
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, sauce_name, sauce_price)
    return sauce

@pytest.fixture (params=IngredientFillingData.data, scope='function')
def ingredient_filling(request):
    filling_name, filling_price = request.param
    filling = Ingredient(INGREDIENT_TYPE_FILLING, filling_name, filling_price)
    return filling

@pytest.fixture (scope='function')
def burger():
    burger = Burger()
    return burger

@pytest.fixture (scope='function')
def database():
    db = Database()
    return db

@pytest.fixture (scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Булочка со специями'
    mock_bun.get_price.return_value = 1.5
    return mock_bun

@pytest.fixture (scope='function')
def mock_ingredient_filling():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = 'Ветчина'
    mock_ingredient.get_type.return_value = 'FILLING'
    mock_ingredient.get_price.return_value = 0.5
    return mock_ingredient

@pytest.fixture (scope='function')
def mock_ingredient_sauce():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = 'Сырный соус'
    mock_ingredient.get_type.return_value = 'SAUCE'
    mock_ingredient.get_price.return_value = 0.75
    return mock_ingredient
