import pytest

from bun import Bun
from data import DataBun


class TestBun:
    @pytest.mark.parametrize('name, price', DataBun.data_create_bun)
    def test_create_bun_success(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name_return_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_price_return_price(self):
        bun = Bun("black bun", 100)
        assert bun.get_price() == 100

