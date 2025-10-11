import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_database_initialization():
    db = Database()
    assert len(db.available_buns()) == 3
    assert len(db.available_ingredients()) == 6


def test_database_available_buns():
    db = Database()
    buns = db.available_buns()
    assert isinstance(buns[0], Bun)
    assert buns[0].get_name() == "black bun"


def test_database_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert isinstance(ingredients[0], Ingredient)
    assert ingredients[0].get_name() == "hot sauce"
    