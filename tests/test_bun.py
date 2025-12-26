import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 50),
            ("white bun", 50),
            ("multi-grain bun", 50),
            ("sesame bun", 50)
        ]
    )
    def test_bun_name(self, name, price):
        assert Bun(name, price).get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("sesame bun", 50),
            ("sesame bun", 300),
            ("sesame bun", 1000),
            ("sesame bun", 100000)
        ]
    )
    def test_bun_price(self, name, price):
        assert Bun(name, price).get_price() == price
