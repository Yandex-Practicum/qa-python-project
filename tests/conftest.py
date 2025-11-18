import pytest
from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture()
def mock_random_choice():
    with patch('random.choice') as mocked_choice:
        yield mocked_choice

@pytest.fixture
def bun():
    return Bun("black bun", 100)

@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)