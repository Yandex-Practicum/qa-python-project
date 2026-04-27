import pytest
from unittest.mock import Mock

from burger import Burger


class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun == bun