import pytest
from praktikum.burger import Burger
from helpers import make_mock_bun, make_mock_ingredient

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    return make_mock_bun()

@pytest.fixture
def mock_ingredient():
    return make_mock_ingredient()

@pytest.fixture
def another_mock_ingredient():
    return make_mock_ingredient(name="Tomato", ing_type="Vegetable", price=0.8)