from praktikum.database import Database
from unittest.mock import Mock
import pytest

@pytest.fixture
def mock_database():
 mock_buns = Mock()
 mock_ingredients = Mock()
 mock_database = Mock(spec=Database)
 mock_database.buns = mock_buns
 mock_database.ingredients = mock_ingredients
 return mock_database

def test_database_init(mock_database):
    mock_database.buns.return_value = [Mock(), Mock(), Mock()]
    mock_database.ingredients.return_value = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
    assert len(mock_database.buns()) == 3
    assert len(mock_database.ingredients()) == 6

def test_database_available_buns(mock_database):
    mock_database.available_buns.return_value = [Mock(), Mock(), Mock()]
    buns = mock_database.available_buns()
    assert len(buns) == 3

def test_database_available_ingredients(mock_database):
    mock_database.available_ingredients.return_value = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
    ingredients = mock_database.available_ingredients()
    assert len(ingredients) == 6

def test_database_init_with_no_data(mock_database):
 mock_database.buns.return_value = []
 mock_database.ingredients.return_value = []
 assert len(mock_database.buns()) == 0
 assert len(mock_database.ingredients()) == 0

