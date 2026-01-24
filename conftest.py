from praktikum.database import Database
from data import Data, Data_1
from unittest.mock import Mock
import pytest


@pytest.fixture
def data_base():
    return Database()


@pytest.fixture()
def mock_for_the_first_bun():
    mock_for_bun = Mock()
    mock_for_bun.get_name.return_value = Data.BUN_NAME
    mock_for_bun.get_price.return_value = Data.PRICE_BUNS
    return mock_for_bun


@pytest.fixture()
def mock_for_the_second_bun():
    mock_for_bun_1 = Mock()
    mock_for_bun_1.get_name.return_value = Data_1.BUN_NAME
    mock_for_bun_1.get_price.return_value = Data_1.PRICE_BUNS
    return mock_for_bun_1


@pytest.fixture()
def mock_sauce_for_the_first_bun():
    mock_for_sauce = Mock()
    mock_for_sauce.get_name.return_value = Data.SAUCES_NAME
    mock_for_sauce.get_price.return_value = Data.SAUCES_PRICE
    mock_for_sauce.get_type.return_value = Data.SAUCES_TYPE
    return mock_for_sauce


@pytest.fixture()
def mock_sauce_for_second_bun():
    mock_for_sauce_1 = Mock()
    mock_for_sauce_1.get_name.return_value = Data_1.SAUCES_NAME
    mock_for_sauce_1.get_price.return_value = Data_1.SAUCES_PRICE
    mock_for_sauce_1.get_type.return_value = Data_1.SAUCES_TYPE
    return mock_for_sauce_1


@pytest.fixture()
def mock_filling_for_the_first_bun():
    mock_for_filling = Mock()
    mock_for_filling.get_name.return_value = Data.FILLING_NAME
    mock_for_filling.get_price.return_value = Data.FILLING_PRICE
    mock_for_filling.get_type.return_value = Data.FILLING_TYPE
    return mock_for_filling


@pytest.fixture()
def mock_filling_for_the_second_bun():
    mock_for_filling_1 = Mock()
    mock_for_filling_1.get_name.return_value = Data_1.FILLING_NAME
    mock_for_filling_1.get_price.return_value = Data_1.FILLING_PRICE
    mock_for_filling_1.get_type.return_value = Data_1.FILLING_TYPE
    return mock_for_filling_1