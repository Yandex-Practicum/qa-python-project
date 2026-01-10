from praktikum.database import Database
from unittest.mock import Mock
from data import Data1, Data2
import pytest


@pytest.fixture
def mock_bun():
    mock_for_bun = Mock()
    mock_for_bun.get_name.return_value = Data1.bun_name
    mock_for_bun.get_price.return_value = Data1.bun_price
    return mock_for_bun


@pytest.fixture
def mock_bun_2():
    mock_for_bun_2 = Mock()
    mock_for_bun_2.get_name.return_value = Data2.bun_name
    mock_for_bun_2.get_price.return_value = Data2.bun_price
    return mock_for_bun_2


@pytest.fixture
def mock_sauce():
    mock_for_sauce = Mock()
    mock_for_sauce.get_name.return_value = Data1.sauce_name
    mock_for_sauce.get_price.return_value = Data1.sauce_price
    mock_for_sauce.get_type.return_value = Data1.sauce_type
    return mock_for_sauce


@pytest.fixture
def mock_sauce_2():
    mock_for_sauce_2 = Mock()
    mock_for_sauce_2.get_name.return_value = Data2.sauce_name
    mock_for_sauce_2.get_price.return_value = Data2.sauce_price
    mock_for_sauce_2.get_type.return_value = Data2.sauce_type
    return mock_for_sauce_2


@pytest.fixture
def mock_filling():
    mock_for_filling = Mock()
    mock_for_filling.get_name.return_value = Data1.filling_name
    mock_for_filling.get_price.return_value = Data1.filling_price
    mock_for_filling.get_type.return_value = Data1.filling_type
    return mock_for_filling


@pytest.fixture
def mock_filling_2():
    mock_for_filling_2 = Mock()
    mock_for_filling_2.get_name.return_value = Data2.filling_name
    mock_for_filling_2.get_price.return_value = Data2.filling_price
    mock_for_filling_2.get_type.return_value = Data2.filling_type
    return mock_for_filling_2


@pytest.fixture
def db():
    return Database()
