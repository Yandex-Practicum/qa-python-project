import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [("black bun", 100.0), ("white bun", 200.5)])
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [("black bun", 100.0), ("white bun", 200.5)])
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price