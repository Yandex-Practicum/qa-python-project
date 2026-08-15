import pytest
from praktikum.bun import Bun


class TestBun:

    def test_bun_creation(self):
        bun = Bun("white bun", 150.5)
        assert bun.name == "white bun"
        assert bun.price == 150.5

    def test_get_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_price(self):
        bun = Bun("red bun", 200)
        assert bun.get_price() == 200
