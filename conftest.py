import pytest
from data import Data, Data_0
from unittest.mock import Mock
from praktikum.database import Database

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = Data.bun_name
    mock_bun.get_price.return_value = Data.bun_price
    return mock_bun

@pytest.fixture
def mock_bun_0():
    mock_bun_0 = Mock()
    mock_bun_0.get_name.return_value = Data_0.bun_name
    mock_bun_0.get_price.return_value = Data_0.bun_price
    return mock_bun_0

@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_name.return_value = Data.sauce_name
    mock_sauce.get_price.return_value = Data.sauce_price
    mock_sauce.get_type.return_value = Data.sauce_type
    return mock_sauce

@pytest.fixture
def mock_sauce_0():
    mock_sauce_0 = Mock()
    mock_sauce_0.get_name.return_value = Data_0.sauce_name
    mock_sauce_0.get_price.return_value = Data_0.sauce_price
    mock_sauce_0.get_type.return_value = Data_0.sauce_type
    return mock_sauce_0

@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_name.return_value = Data.filling_name
    mock_filling.get_price.return_value = Data.filling_price
    mock_filling.get_type.return_value = Data.filling_type
    return mock_filling

@pytest.fixture
def mock_filling_0():
    mock_filling_0 = Mock()
    mock_filling_0.get_name.return_value = Data_0.filling_name
    mock_filling_0.get_price.return_value = Data_0.filling_price
    mock_filling_0.get_type.return_value = Data_0.filling_type
    return mock_filling_0

@pytest.fixture
def data_base():
    return Database()