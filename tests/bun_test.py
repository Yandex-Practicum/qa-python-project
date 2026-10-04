import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100.0),
            ("white bun", 200.0),
            ("red bun", 300.0),
            ("", 0.0),
        ],
    )
    def test_bun_init_and_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_attributes(self):
        bun = Bun("black bun", 100.0)
        assert bun.name == "black bun"
        assert bun.price == 100.0