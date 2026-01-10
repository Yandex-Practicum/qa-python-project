import pytest
from praktikum.bun import *

class TestBun:

    @pytest.mark.parametrize("bun_name, bun_price",
                             [
                                 ("Ржаная", 80.5),
                                 ("Пшеничная", 70.0)
                             ])
    def test_init_correct_types_and_values(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert isinstance(bun.name, str)
        assert isinstance(bun.price, float)
        assert bun.name == bun_name
        assert bun.price == bun_price

    def test_get_bun_name_returns_name(self, bun):
        bun.get_name()
        assert bun.get_name() == "Ржаная"

    def test_get_bun_price_returns_price(self, bun):
        bun.get_price()
        assert bun.get_price() == 80.5
