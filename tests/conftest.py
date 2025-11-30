import random
from unittest.mock import Mock
import pytest

from helpers.helpers import generate_random_string
from praktikum import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture(scope='function')
def bun_mock():
    bun_mock = Mock()
    bun_mock.name = generate_random_string(10)
    bun_mock.price = float(random.randint(1, 1000))
    bun_mock.get_price.return_value = bun_mock.price
    bun_mock.get_name.return_value = bun_mock.name

    return bun_mock


@pytest.fixture(scope='function')
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.name = generate_random_string(10)
    ingredient_mock.price = float(random.randint(1, 1000))
    ingredient_mock.get_price.return_value = ingredient_mock.price
    ingredient_mock.get_type.return_value = ingredient_mock.type
    ingredient_mock.get_name.return_value = ingredient_mock.name

    return ingredient_mock


@pytest.fixture(scope='function')
def sauce_mock():
    sauce_mock = Mock()
    sauce_mock.type = INGREDIENT_TYPE_SAUCE
    sauce_mock.name = generate_random_string(10)
    sauce_mock.price = float(random.randint(1, 1000))
    sauce_mock.get_price.return_value = sauce_mock.price
    sauce_mock.get_type.return_value = sauce_mock.type
    sauce_mock.get_name.return_value = sauce_mock.name

    return sauce_mock


@pytest.fixture(scope='function')
def filling_mock():
    filling_mock = Mock()
    filling_mock.type = INGREDIENT_TYPE_FILLING
    filling_mock.name = generate_random_string(10)
    filling_mock.price = float(random.randint(1, 1000))
    filling_mock.get_price.return_value = filling_mock.price
    filling_mock.get_type.return_value = filling_mock.type
    filling_mock.get_name.return_value = filling_mock.name

    return filling_mock

