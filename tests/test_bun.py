import pytest
from praktikum.bun import Bun
from permanent import Permanent


class TestBun:

    @pytest.mark.parametrize("bun_name,bun_price", Permanent.BUNS)
    def test_bun_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.name == bun_name

    @pytest.mark.parametrize("bun_name,bun_price", Permanent.BUNS)
    def test_bun_price(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.price == bun_price