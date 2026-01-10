import pytest
from database import Database
from bun import Bun
from ingredient import Ingredient

@pytest.fixture
def db():
    return Database()

def test_database_buns(db):
    buns = db.available_buns()
    assert len(buns) == 3
    assert isinstance(buns[0], Bun)

def test_database_ingredients(db):
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert isinstance(ingredients[0], Ingredient)
