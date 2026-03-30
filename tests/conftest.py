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
    ing_a = Mock()
    ing_a.get_name.return_value = "Ingredient_A"
    ing_a.get_type.return_value = "FILLING"
    ing_a.get_price.return_value = 10
    return ing_a


@pytest.fixture
def mock_ingredient_b():
    ing_b = Mock()
    ing_b.get_name.return_value = "Ingredient_B"
    ing_b.get_type.return_value = "FILLING"
    ing_b.get_price.return_value = 10
    return ing_b


@pytest.fixture
def mock_ingredient_c():
    ing_c = Mock()
    ing_c.get_name.return_value = "Ingredient_C"
    ing_c.get_type.return_value = "FILLING"
    ing_c.get_price.return_value = 10
    return ing_c

