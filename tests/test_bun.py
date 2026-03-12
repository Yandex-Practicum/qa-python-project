import pytest

from praktikum.bun import Bun
from tests.data import BUN


class TestBun:

    @pytest.mark.parametrize('name, price', BUN)
    def test_get_name_returns_correct_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', BUN)
    def test_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price