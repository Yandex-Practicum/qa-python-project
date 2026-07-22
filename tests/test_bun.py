import pytest
from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_name_different_bun(self):
        bun = Bun("white bun", 200)
        assert bun.get_name() == "white bun"

    def test_get_price(self):
        bun = Bun("black bun", 100)
        assert bun.get_price() == 100

    def test_get_price_different_bun(self):
        bun = Bun("red bun", 300)
        assert bun.get_price() == 300

    def test_bun_creation_get_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_bun_creation_get_price(self):
        bun = Bun("white bun", 200)
        assert bun.get_price() == 200


        