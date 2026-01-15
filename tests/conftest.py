import pytest
from praktikum.database import Database
from unittest.mock import MagicMock
from praktikum.burger import Burger



@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 200
    return bun

@pytest.fixture
def mock_ingredient():
    """Замоканный ингредиент."""
    ingredient = MagicMock()
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_price.return_value = 100
    ingredient.get_type.return_value = "Filling"
    return ingredient

@pytest.fixture
def mock_ingredients():
    ingredients = []
    for i in range(3):
        ingredient = MagicMock()
        ingredient.get_name.return_value = f"Ingredient {i}"
        ingredient.get_price.return_value = 100 + i * 50
        ingredient.get_type.return_value = "Filling" if i % 2 == 0 else "Sauce"
        ingredients.append(ingredient)
    return ingredients




