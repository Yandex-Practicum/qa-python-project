import pytest
from unittest.mock import Mock
from burger import Burger
from data import *


#пустой объект Burger
@pytest.fixture
def new_burger():
    return Burger()

# Мок-булка 
@pytest.fixture
def bun_in_burger():
    bun = Mock()
    bun.name = BUN_DATA["name"]
    bun.price = BUN_DATA["price"]
    bun.get_price.return_value = BUN_DATA["price"]
    bun.get_name.return_value = BUN_DATA["name"]
    return bun

# список для бургера
@pytest.fixture
def ingredients_in_burger():
    ingredients = []
    for i in INGREDIENTS_DATA:
        ingredient = Mock()
        ingredient.type = i["type"]
        ingredient.name = i["name"]
        ingredient.price = i["price"]
        ingredient.get_type.return_value = i["type"]
        ingredient.get_name.return_value = i["name"]
        ingredient.get_price.return_value = i["price"]
        ingredients.append(ingredient)
    return ingredients

# мок с булкой и ингредиентами
@pytest.fixture
def mocked_burger(new_burger, bun_in_burger, ingredients_in_burger):
    new_burger.set_buns(bun_in_burger)
    new_burger.ingredients = ingredients_in_burger.copy()
    return new_burger