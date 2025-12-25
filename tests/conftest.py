import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mocked_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    return bun

@pytest.fixture
def mocked_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50

    return ingredient

@pytest.fixture
def mocked_ingredients_list():
    ingredients = []
    for i in (10,20,30):
        ingredient = Mock()
        ingredient.get_price.return_value = i
        ingredients.append(ingredient)

    return ingredients
