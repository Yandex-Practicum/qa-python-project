from praktikum.bun import Bun
import pytest


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price
