import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("Black bun", 100.0),
        ("White bun", 200.0),
        ("Red bun", 300.0)
    ])
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("Black bun", 100.0),
        ("White bun", 200.0),
        ("Red bun", 300.0)
    ])
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
