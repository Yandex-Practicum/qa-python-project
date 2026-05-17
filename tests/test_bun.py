import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name,price",
        [
            ("black bun", 100),
            ("white bun", 200),
        ],
    )
    def test_get_name_returns_bun_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name,price",
        [
            ("black bun", 100),
            ("red bun", 300),
        ],
    )
    def test_get_price_returns_bun_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price
