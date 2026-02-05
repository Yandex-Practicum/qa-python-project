from unittest.mock import Mock
import pytest
from data import BUN_NAME, BUN_PRICE, INGREDIENT_NAME, INGREDIENT_PRICE
from practicum.bun import Bun
from practicum.burger import Burger
from practicum.database import Database
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def bun_fixture():
    name = BUN_NAME
    price = BUN_PRICE
    bun = Bun(name, price)    
    return bun

@pytest.fixture()
def ingredient_fixture():
    type = INGREDIENT_TYPE_SAUCE
    name = INGREDIENT_NAME
    price = INGREDIENT_PRICE  
    ingredient = Ingredient(type, name, price)    
    return ingredient

@pytest.fixture()
def burger_empty():
    burger = Burger()
    return burger

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = INGREDIENT_NAME
    ingredient.get_price.return_value = INGREDIENT_PRICE
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient

@pytest.fixture
def burger_full(mock_bun, mock_ingredient):
    burger = Burger()
    burger.bun = mock_bun
    burger.ingredients = [mock_ingredient]
    return burger

@pytest.fixture
def database_fixture():
    database = Database()
    return database