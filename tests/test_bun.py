import pytest 
from praktikum.bun import Bun
from data import BunData
#python -B -m pytest tests/test_bun.py
#python -m pytest --cov=praktikum tests/

class TestBun:
    @pytest.mark.parametrize(
    "name, price",
    [
        (BunData.black_bun[0], BunData.black_bun[1]),
        (BunData.white_bun[0], BunData.white_bun[1]),
        (BunData.red_bun[0], BunData.red_bun[1])
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
    "name, price",
    [
        (BunData.black_bun[0], BunData.black_bun[1]),
        (BunData.white_bun[0], BunData.white_bun[1]),
        (BunData.red_bun[0], BunData.red_bun[1])
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price