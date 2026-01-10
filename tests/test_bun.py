from praktikum.bun import Bun
import pytest
from data import bun_name, bun_price


class TestBun:

    def test_get_name_success(self, bun):
        assert bun.get_name() == bun_name

    def test_get_price_success(self, bun):
        assert bun.get_price() == bun_price
