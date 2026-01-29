from unittest.mock import Mock

import allure
import pytest

from data import BUN_NAME, BUN_PRICE, BUN2_NAME, BUN2_PRICE


@allure.title('bun1 mock')
@pytest.fixture
def setup_bun():
    mock_bun = Mock()
    mock_bun.name = BUN_NAME
    mock_bun.price = BUN_PRICE
    mock_bun.return_value.get_name = BUN_NAME
    mock_bun.return_value.get_price = BUN_PRICE
    return mock_bun

@allure.title('bun2 mock')
@pytest.fixture
def setup_bun2():
    mock_bun = Mock()
    mock_bun.name = BUN2_NAME
    mock_bun.price = BUN2_PRICE
    mock_bun.return_value.get_name = BUN2_NAME
    mock_bun.return_value.get_price = BUN2_PRICE
    return mock_bun