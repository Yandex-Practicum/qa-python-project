from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient import Ingredient
from data.ingredient_data import INGREDIENT_NAME_SAUCE, INGREDIENT_PRICE_SAUCE
from praktikum.database import Database 
from praktikum.burger import Burger
from data.bun_data import BUN_NAME, BUN_PRICE
from unittest.mock import Mock
import pytest

@pytest.fixture()
def bun():
    return Bun(BUN_NAME, BUN_PRICE)

@pytest.fixture()
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME_SAUCE, INGREDIENT_PRICE_SAUCE)

@pytest.fixture()
def burger():
    burger = Burger()
    return burger

@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = BUN_PRICE 
    mock_bun.get_name.return_value = BUN_NAME
    return mock_bun 

@pytest.fixture()
def database():
    database = Database()
    return database

@pytest.fixture()
def make_ingredient():
    def create_mock(name=INGREDIENT_NAME_SAUCE, price=INGREDIENT_PRICE_SAUCE, type=INGREDIENT_TYPE_SAUCE):
        mock = Mock()
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        mock.get_type.return_value = type
        return mock
    return create_mock
