from unittest.mock import Mock
from data import BUN_NAME, BUN_PRICE, BUN_NAME1, BUN_PRICE1, BUN_NAME2, BUN_PRICE2,SAUCE_NAME, SAUCE_PRICE, FILLING_NAME, FILLING_PRICE
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.name = BUN_NAME
    mock.price = BUN_PRICE
    mock.get_name.return_value = BUN_NAME
    mock.get_price.return_value = BUN_PRICE
    return mock


@pytest.fixture()
def some_ingredients(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    ingredient_1 = Ingredient(ingredient_type="соус", name=SAUCE_NAME, price=SAUCE_PRICE)
    ingredient_2 = Ingredient(ingredient_type="начинка", name=FILLING_NAME, price=FILLING_PRICE)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    return burger


@pytest.fixture()
def database_with_buns_ingredients():
    database = Database()
    database.buns.append(Bun(BUN_NAME, BUN_PRICE))
    database.buns.append(Bun(BUN_NAME1, BUN_PRICE1))
    database.buns.append(Bun(BUN_NAME2, BUN_PRICE2))
    database.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE))
    database.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE))
    return database

