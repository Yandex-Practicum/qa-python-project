from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

from unittest.mock import Mock
import pytest


@pytest.fixture
def burger_instance():
    burger = Burger()
    return burger


@pytest.fixture
def mock_bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = 'Test Bun Name'
    bun_mock.get_price.return_value = 1000
    return bun_mock


@pytest.fixture
def mock_ingredient():
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_name.return_value = "Test Ingredient Name"
    ingredient_mock.get_price.return_value = 50
    return ingredient_mock


@pytest.fixture
def mock_two_ingredient():
    ingredient_two_mock = Mock()
    ingredient_two_mock.get_type.return_value = "SAUCE"
    ingredient_two_mock.get_name.return_value = "Test Ingredient Name"
    ingredient_two_mock.get_price.return_value = 70
    return ingredient_two_mock


@pytest.fixture
def mock_ingredient_a():
    ingredient_a_mock = Mock()
    ingredient_a_mock.get_name.return_value = "A"
    return ingredient_a_mock


@pytest.fixture
def mock_ingredient_b():
    ingredient_b_mock = Mock()
    ingredient_b_mock.get_name.return_value = "B"
    return ingredient_b_mock


@pytest.fixture
def mock_ingredient_c():
    ingredient_c_mock = Mock()
    ingredient_c_mock.get_name.return_value = "C"
    return ingredient_c_mock

