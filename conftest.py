import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def db():
    db = Database()
    return db

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 100.0
    return bun

@pytest.fixture
def mock_ingredients():
    ingredients = []
    for i in range(3):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = f"ingredient_{i}"
        ingredient.get_price.return_value = float(50 * (i + 1))
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE if i % 2 == 0 else INGREDIENT_TYPE_FILLING
        ingredients.append(ingredient)
    return ingredients