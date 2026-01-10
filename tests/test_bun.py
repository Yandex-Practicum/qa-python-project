import pytest
from praktikum.bun import Bun

class TestBun:
    #тест  гетеров
    def test_bun_get_name_returns_value(self):
        bun = Bun("red bun", 450)
        assert bun.get_name() == "red bun"

    def test_bun_get_price_returns_value(self):
        bun = Bun("red bun", 450)
        assert bun.get_price() == 450

    @pytest.mark.parametrize(
        "name, price",
        [
            ("white bun", 0),
            ("red bun", 300),
            ("yellow bun", 10.99)
        ]
    )
    def test_bun_get_name_parametrized(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("white bun", 0),
            ("red bun", 300),
            ("yellow bun", 10.99)
        ]
    )
    def test_bun_get_price_parametrized(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price





