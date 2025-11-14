import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import MagicMock
from prakticum.bun import Bun
from prakticum.ingredient import Ingredient
from prakticum.burger import Burger




@pytest.fixture
def burger():
    """Для создания экземпляра бургера."""
    return Burger()


@pytest.fixture
def mock_bun():
    """Для создания булочки."""
    return Bun("Sesame Bun", 2.5)


@pytest.fixture
def mock_ingredient():
    """Для создания ингредиента."""
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = 'Cheese'
    ingredient.get_price.return_value = 1.0
    ingredient.get_type.return_value = 'cheese'
    return ingredient


@pytest.fixture
def multiple_ingredients():
    """Для создания нескольких ингредиентов."""
    ingredient1 = MagicMock(spec=Ingredient)
    ingredient1.get_name.return_value = 'Cheese'
    ingredient1.get_price.return_value = 1.0
    ingredient1.get_type.return_value = 'cheese'

    ingredient2 = MagicMock(spec=Ingredient)
    ingredient2.get_name.return_value = 'Lettuce'
    ingredient2.get_price.return_value = 0.5
    ingredient2.get_type.return_value = 'vegetable'

    ingredient3 = MagicMock(spec=Ingredient)
    ingredient3.get_name.return_value = 'Tomato'
    ingredient3.get_price.return_value = 0.7
    ingredient3.get_type.return_value = 'vegetable'

    return [ingredient1, ingredient2, ingredient3]

