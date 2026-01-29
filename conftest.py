import pytest
from bun import Bun
from ingredient import Ingredient
from database import Database


@pytest.fixture
def sesame_bun():
    return Bun("Sesame Bun", 50.0)


@pytest.fixture
def lettuce_ingredient():
    return Ingredient("FILLING", "Lettuce", 10.0)


@pytest.fixture
def tomato_ingredient():
    return Ingredient("FILLING", "Tomato", 15.0)


@pytest.fixture
def db():
    return Database()
