import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize(
    "name",
    [
        "white bun",
        "black bun",
        "red bun"
    ]
)
    def test_get_name(self, name):
        bun = Bun(name, 200)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [
            100,
            200,
            300
        ]
    )
    def test_get_price(self, price):
        bun = Bun("white bun", price)
        assert bun.get_price() == price
        