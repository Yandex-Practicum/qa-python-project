from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    return bun
    