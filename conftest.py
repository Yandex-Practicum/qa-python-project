from unittest.mock import Mock
import pytest
from data import BUN_DATA, SAUCE_DATA
from practicum.bun import Bun
from practicum.burger import Burger
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def bun_fixture():
    name = list(BUN_DATA.keys())[0]
    price = BUN_DATA[name]
    bun = Bun(name, price)    
    return bun

@pytest.fixture()
def ingredient_fixture():
    type = INGREDIENT_TYPE_SAUCE
    name = list(SAUCE_DATA.keys())[0]
    price = SAUCE_DATA[name]    
    ingredient = Ingredient(type, name, price)    
    return ingredient

@pytest.fixture()
def burger_empty():
    burger = Burger()
    return burger

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = list(BUN_DATA.keys())[0]
    bun.get_price.return_value = BUN_DATA[list(BUN_DATA.keys())[0]]
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = list(SAUCE_DATA.keys())[0]
    ingredient.get_price.return_value = SAUCE_DATA[list(SAUCE_DATA.keys())[0]]
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient

@pytest.fixture
def burger_full(mock_bun, mock_ingredient):
    burger = Burger()
    burger.bun = mock_bun
    burger.ingredients = [mock_ingredient]
    return burger