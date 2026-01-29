import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from helpers import SAUCE_NAME, FILLING_NAME, SAUCE_PRICE, FILLING_PRICE, create_mock_ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    return Mock(spec=Bun)


@pytest.fixture
def mock_ingredient():
    return Mock(spec=Ingredient)


@pytest.fixture
def mock_sauce():
    return create_mock_ingredient(SAUCE_NAME, SAUCE_PRICE)


@pytest.fixture
def mock_filling():
    return create_mock_ingredient(FILLING_NAME, FILLING_PRICE)
