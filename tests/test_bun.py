import pytest
from praktikum.bun import Bun

class TestBun:
    def test_bun_name(self, sample_bun):
        expected_name = "green"
        actual_name = sample_bun.get_name()
        assert actual_name == expected_name

    def test_bun_price(self, sample_bun):
        expected_price = 10
        actual_price = sample_bun.get_price()
        assert actual_price == expected_price

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])

    def test_bun_creation(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name
        assert  bun.get_price() == price


