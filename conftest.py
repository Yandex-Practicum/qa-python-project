from unittest.mock import patch

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_database():
    with patch('praktikum.database.Database') as MockDatabase:
        mock_db = MockDatabase.return_value
        mock_db.buns = [
            Bun('black bun', 100),
            Bun('white bun', 200),
            Bun('red bun', 300),
        ]
        mock_db.ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
            Ingredient(INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            Ingredient(INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
            Ingredient(INGREDIENT_TYPE_FILLING, 'sausage', 300),
        ]
        return mock_db
