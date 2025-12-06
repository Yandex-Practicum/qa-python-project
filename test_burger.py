import pytest
from burger import Burger


class TestBurger:

    def test_add_bun_at_order(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

