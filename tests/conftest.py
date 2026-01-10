import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def empty_burger():
    return Burger()

@pytest.fixture
def ketchup():
    return Ingredient(INGREDIENT_TYPE_SAUCE, 'Кетчуп', 3.50)

@pytest.fixture
def mayonnaise():
    return Ingredient(INGREDIENT_TYPE_SAUCE, 'Майонез', 2.50)

@pytest.fixture
def cucumber():
    return Ingredient(INGREDIENT_TYPE_FILLING, 'Огурец', 1.50)

@pytest.fixture
def kunzhutnaya_bun():
    return Bun("Кунжутная", 3.50)

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_database():
    database = Mock(spec=Database)

    mock_buns = [Mock(spec=Bun) for _ in range(3)]
    database.available_buns.return_value = mock_buns

    mock_ingredients = [Mock(spec=Ingredient) for _ in range(6)]
    database.available_ingredients.return_value = mock_ingredients

    return database
