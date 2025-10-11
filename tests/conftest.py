import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    mock_bun = Mock(Bun)
    mock_bun.name = 'Булочка с кокосовой стружкой'
    mock_bun.price = 400
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock(Ingredient)
    mock_ingredient.type = 'Начинка'
    mock_ingredient.name = 'Ломтик Лосося'
    mock_ingredient.price = 500
    return mock_ingredient

@pytest.fixture
def database():
    mock_database = Mock(Database)
    mock_database.buns.append(['white bun', 200])
    mock_database.ingredients = 1
    return mock_database
