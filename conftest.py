import pytest
from unittest.mock import Mock

from unittest.mock import patch
from data.bun_data import BunData
from data.burger_data import BurgerData
from data.ingredient_data import IngredientData
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

@patch('bun.Burger', return_value = ['tets', 456])
@pytest.fixture(scope='function')
def mock_database():
    data = Database()
    return data

@pytest.fixture(scope='function')
def ibgredient():
    ingredient = Ingredient(IngredientData.type, IngredientData.name, IngredientData.price)
    return ingredient

@pytest.fixture(scope='function')
def create_bun():
    bun = Bun(name = BunData.bun, price= BunData.price)
    return bun

@pytest.fixture(scope='function')
def data_base_mock():
    mock_data = Mock()
    mock_data.return_value = [Bun("black bun", 100)]
    return mock_data

@pytest.fixture(scope='function')
def add_ingredient():
    burger = Burger()
    burger.add_ingredient(BurgerData.ingredient_name)
    return burger

@pytest.fixture(scope='function')
def add_ingredient_two():
    burger = Burger()
    burger.add_ingredient(BurgerData.ingredient_name)
    burger.add_ingredient(BurgerData.ingredient_type_meet)
    return burger

@pytest.fixture(scope='function')
def ingredient_mock():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = BurgerData.ingredient_price
    mock_ingredient.get_name.return_value = BurgerData.ingredient_name
    mock_ingredient.get_type.return_value = BurgerData.ingredient_type
    return mock_ingredient

@pytest.fixture(scope='function')
def bun_mock():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BunData.bun
    mock_bun.get_price.return_value = BunData.price
    return mock_bun

