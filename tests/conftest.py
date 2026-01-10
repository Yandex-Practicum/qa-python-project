import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


@pytest.fixture
def bun():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = "Cheese Burger"
    bun_mock.get_price.return_value = 10.22
    return bun_mock
