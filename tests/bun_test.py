from conftest import bun
from data import bun_test


class TestBun:
    def test_get_name(self, bun):
        assert bun.get_name() == bun_test["name"]

    def test_get_price(self, bun):
         assert bun.get_price() == bun_test["price"]
