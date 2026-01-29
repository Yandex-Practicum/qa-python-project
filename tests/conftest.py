import pytest
from unittest.mock import Mock
from data import *
from praktikum.database import Database
from praktikum.burger import Burger

@pytest.fixture
def mock_bun():
    mock_buns = Mock()
    mock_buns.get_name.return_value = Data.Bun_name
    mock_buns.get_price.return_value = Data.Bun_price
    return mock_buns

@pytest.fixture
def mock_sauce():
    mock_sauces = Mock()
    mock_sauces.get_name.return_value = Data.Sauce_name
    mock_sauces.get_price.return_value = Data.Sauce_price
    mock_sauces.get_type.return_value = Data.Sauce_type
    return mock_sauces

@pytest.fixture
def mock_filling():
    mock_fillings = Mock()
    mock_fillings.get_name.return_value = Data.Filling_name
    mock_fillings.get_price.return_value = Data.Filling_price
    mock_fillings.get_type.return_value = Data.Filling_type
    return mock_fillings

@pytest.fixture
def data_base_fixture():
    return Database()

@pytest.fixture
def burger_fixture(mock_bun):
    burger=Burger()
    burger.set_buns(mock_bun)
    return burger

