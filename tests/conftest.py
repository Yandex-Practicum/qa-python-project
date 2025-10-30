import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    """Create a database instance for testing."""
    return Database()


@pytest.fixture
def empty_burger():
    """Create an empty burger for testing."""
    return Burger()


@pytest.fixture
def test_bun():
    """Create a test bun for testing."""
    return Bun("test bun", 100.0)


@pytest.fixture
def sauce_ingredient():
    """Create a sauce ingredient for testing."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50.0)


@pytest.fixture
def filling_ingredient():
    """Create a filling ingredient for testing."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "test filling", 150.0)