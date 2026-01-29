from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture(scope='function')
def mock_ingredient1():
    mock_ingredient1 = Mock()
    mock_ingredient1.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient1.name = 'Ingredient1'
    mock_ingredient1.price = 100

    return mock_ingredient1


@pytest.fixture(scope='function')
def mock_ingredient2():
    mock_ingredient2 = Mock()
    mock_ingredient2.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient2.name = 'Ingredient2'
    mock_ingredient2.price = 100

    return mock_ingredient2


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = 'TestBun'
    mock_bun.price = 100

    return mock_bun


@pytest.fixture(scope='function')
def burger(mock_ingredient1, mock_ingredient2):
    burger = Burger()
    burger.add_ingredient(mock_ingredient1)
    burger.add_ingredient(mock_ingredient2)
    return burger
