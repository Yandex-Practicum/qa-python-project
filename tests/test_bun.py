import pytest
import bun
import data


class TestBun:

    def test_get_name_success(self):
        bun_1 = bun.Bun(data.random_bun, data.random_price_int)

        assert bun_1.get_name() == data.random_bun

    @pytest.mark.parametrize("bun_name, price", [
        (data.random_bun, data.random_price_int),
        (data.random_bun, data.random_price_float)
    ])
    def test_get_price_success(self,bun_name, price):
        bun_1 = bun.Bun(bun_name, price)

        assert bun_1.get_price() == price


