import pytest
from praktikum.bun import Bun
from data import BUN_TEST_CASES

class TestBunAttributes:
    @pytest.mark.parametrize("name, price", BUN_TEST_CASES)
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_TEST_CASES)
    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    def test_bun_with_zero_price(self):
        bun = Bun("ZeroPrice", 0)
        assert bun.get_name() == "ZeroPrice"

    def test_bun_with_zero_price_value(self):
        bun = Bun("ZeroPrice", 0)
        assert bun.get_price() == 0

    def test_bun_with_empty_name(self):
        bun = Bun("", 10)
        assert bun.get_name() == ""

    def test_bun_with_name(self):
        bun = Bun("TestName", 10)
        assert bun.get_name() == "TestName"

    def test_bun_with_price(self):
        bun = Bun("TestName", 10)
        assert bun.get_price() == 10
