import pytest
from unittest.mock import Mock
from data import bun_price, bun_name
@pytest.fixture # фикстура, которая создаёт мок-булку
def item_of_mock_bun_class():
    mock_bun = Mock()
    mock_bun.get_name.return_value = bun_name
    mock_bun.get_price.return_value = bun_price
    return mock_bun