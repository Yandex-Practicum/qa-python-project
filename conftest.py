from unittest.mock import Mock
import pytest
from data import BunData, IngredientData, RemoveIngredientData
from praktikum.burger import Burger
from praktikum.database import Database

@pytest.fixture(scope='function')
def cosmo_burger():
    return Burger()

@pytest.fixture(scope='function')
def bun_mock():
    bun = Mock()
    bun.get_price.return_value = BunData.price
    bun.get_name.return_value = BunData.name
    return bun

@pytest.fixture(scope='function')
def ingredient_mock():
    ingredient = Mock()
    ingredient.get_price.return_value = IngredientData.price
    ingredient.get_name.return_value = IngredientData.name
    ingredient.get_type.return_value = IngredientData.type
    return ingredient

@pytest.fixture(scope='function')
def ingredient_mock_remove():
    ingredient = Mock()
    ingredient.get_price.return_value = RemoveIngredientData.price
    ingredient.get_name.return_value = RemoveIngredientData.name
    ingredient.get_type.return_value = RemoveIngredientData.type
    return ingredient

@pytest.fixture(scope='function')
def data_base_mock():
    return Database()
