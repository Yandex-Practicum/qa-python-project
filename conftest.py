import pytest
from data import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture()
def mock_bun():
    return MockBun.get_mock_bun()

@pytest.fixture()
def mock_sauce():
    return MockIngredient.get_mock_ingredient(
        INGREDIENT_TYPE_SAUCE,
        AvailableIngredients.sauces[0]['name'],
        AvailableIngredients.sauces[0]['price']
    )

@pytest.fixture()
def mock_filling():
    return MockIngredient.get_mock_ingredient(
        INGREDIENT_TYPE_FILLING,
        AvailableIngredients.fillings[0]['name'],
        AvailableIngredients.fillings[0]['price']
    )
