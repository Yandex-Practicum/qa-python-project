from unittest.mock import Mock
import pytest
from data import TestBurgerData
from praktikum.database import Database


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = TestBurgerData.bun_name
    mock_bun.get_price.return_value = TestBurgerData.bun_price
    return mock_bun

@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_name.return_value = TestBurgerData.filling_name
    mock_filling.get_price.return_value = TestBurgerData.filling_price
    mock_filling.get_type.return_value = TestBurgerData.filling_type
    return mock_filling

@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_name.return_value = TestBurgerData.sauce_name
    mock_sauce.get_price.return_value = TestBurgerData.sauce_price
    mock_sauce.get_type.return_value = TestBurgerData.sauce_type
    return mock_sauce

@pytest.fixture
def database():
    return Database()