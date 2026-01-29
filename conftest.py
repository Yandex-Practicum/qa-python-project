import pytest
import random
from unittest.mock import Mock
from data import *
from praktikum.database import Database

@pytest.fixture
def mock_bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = KratornayaBun.bun_name
    bun_mock.get_price.return_value = KratornayaBun.bun_price
    return bun_mock


@pytest.fixture
def mock_sauce():
    sauce_type, sauce_name, sauce_price = random.choice(Ingredients.sauces)
    sauce_mock = Mock()

    sauce_mock.get_name.return_value = sauce_name
    sauce_mock.get_price.return_value = sauce_price
    sauce_mock.get_type.return_value = sauce_type
    return sauce_mock


@pytest.fixture
def mock_filling():
    filling_type, filling_name, filling_price = random.choice(Ingredients.fillings)
    filling_mock = Mock()

    filling_mock.get_name.return_value = filling_name
    filling_mock.get_price.return_value = filling_price
    filling_mock.get_type.return_value = filling_type
    return filling_mock

@pytest.fixture
def db():
    return Database()