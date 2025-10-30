import pytest
from data import data
from praktikum.bun import Bun


class TestBun:
    def test_create_bun_with_name_and_price(self, bun):
        assert bun.name == data.bun_name
        assert bun.price == data.bun_price

    def test_get_name_bun_success(self, bun):
        assert bun.get_name() == data.bun_name

    def test_get_price_bun_success(self, bun):
        assert bun.get_price() == data.bun_price
