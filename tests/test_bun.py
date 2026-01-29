import pytest
from data import *
from praktikum.bun import Bun


@pytest.mark.parametrize("data", [FluorescentBun, KratornayaBun])
class TestBun:
    def test_name_bun(self,data):
        bun = Bun(data.bun_name, data.bun_price)
        assert bun.get_name() == data.bun_name, f'Expected name: {data.bun_name}, but got: {bun.get_name()}'


    def test_price_bun(self,data):
        bun = Bun(data.bun_name, data.bun_price)
        assert bun.get_price() == data.bun_price, f'Expected price: {data.bun_price}, but got: {bun.get_price()}'