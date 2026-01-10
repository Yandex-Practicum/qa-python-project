import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock 


@pytest.fixture
def bun():
    bun = Bun(name = 'bulochka', price = 150)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(ingredient_type='main', name = 'beef', price = 300)
    return ingredient

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.ingredient_type='main'
    ingredient.price = 300
    return ingredient

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.name = 'bulochka'
    bun.price = 150
    return bun

@pytest.fixture
def mock_burger(mock_bun, mock_ingredient):
    burger = Mock()
    burger.bun = mock_bun
    burger.ingredient = mock_ingredient
    return burger
