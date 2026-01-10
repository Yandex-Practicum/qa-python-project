import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from data import Data
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    burger = Burger()
    bun = MagicMock(spec=Bun)
    bun.get_name.return_value = Data.BUNS[0][0]
    bun.get_price.return_value = Data.BUNS[0][1]
    burger.set_buns(bun)
    return burger



@pytest.fixture
def ingredient1():
    ingredient_type, ingredient_name, ingredient_price = Data.INGREDIENTS[0]
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = ingredient_name
    ingredient.get_price.return_value = ingredient_price
    ingredient.get_type.return_value = ingredient_type
    return ingredient

@pytest.fixture
def ingredient2():
    ingredient_type, ingredient_name, ingredient_price = Data.INGREDIENTS[1]
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = ingredient_name
    ingredient.get_price.return_value = ingredient_price
    ingredient.get_type.return_value = ingredient_type
    return ingredient