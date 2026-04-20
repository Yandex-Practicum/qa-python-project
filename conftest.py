from ingredient import Ingredient
from burger import Burger
from database import Database
import pytest
import data
from unittest.mock import Mock
import ingredient_types
from bun import Bun


@pytest.fixture(params=[('Пшеничная булка', 890),
                        ('Кукурузная булка', 1689)])
def bun(request):
    name, price = request.param
    bun = Bun(name, price)
    return bun, name, price


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = 'Ржаная булка'
    mock_bun.price = 1200
    return mock_bun


@pytest.fixture(params=[(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус майонезный', 50),
                        (ingredient_types.INGREDIENT_TYPE_FILLING, 'Киви', 100)])
def ingredient(request):
    ingredient_type, name, price = request.param
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient, ingredient_type, name, price


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def burger_with_bun_and_ingredients():
    burger = Burger()
    for n in data.ingredients:
        ingredient_type, name, price = n
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)
    bun = Bun(*data.bun)
    burger.set_buns(bun)

    return burger


@pytest.fixture
def database():
    database = Database()
    return database
