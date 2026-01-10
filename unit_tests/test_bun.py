import pytest

from bun import Bun
from database import Database


@pytest.mark.parametrize("bun", Database().available_buns())
class TestBun:
    def test_bun_creation(self, bun):
        new_bun = Bun(name=bun.name, price=bun.price)
        assert new_bun.name == bun.name
        assert new_bun.price == bun.price

    def test_get_name(self, bun):
        new_bun = Bun(name=bun.name, price=bun.price)
        assert new_bun.get_name() == bun.name

    def test_get_price(self, bun):
        new_bun = Bun(name=bun.name, price=bun.price)
        assert new_bun.get_price() == bun.price
