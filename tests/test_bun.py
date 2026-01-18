import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name, price",
        [
            ("name_1", 100),
            ("name_2", 100),
            ("name_3", 100),
        ]
    )
    def test_get_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("name", 100),
            ("name", 200),
            ("name", 300),
        ]
    )
    def test_get_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price
