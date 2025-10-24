import pytest
from tests import data
from praktikum.bun import Bun


class TestBun:

    def test_get_name_returns_correct_name(self):
        bun = Bun(data.BunData.BLACK_BUN["name"], data.BunData.BLACK_BUN["price"])
        assert bun.get_name() == data.BunData.BLACK_BUN["name"]

    def test_get_price_returns_correct_price(self):
        bun = Bun(data.BunData.WHITE_BUN["name"], data.BunData.WHITE_BUN["price"])
        assert bun.get_price() == data.BunData.WHITE_BUN["price"]

    def test_bun_with_zero_price(self):
        bun = Bun(data.BunData.FREE_BUN["name"], data.BunData.FREE_BUN["price"])
        assert bun.get_price() == data.BunData.FREE_BUN["price"]

    def test_bun_with_special_characters_in_name(self):
        bun = Bun(data.BunData.SPECIAL_CHAR_BUN["name"], data.BunData.SPECIAL_CHAR_BUN["price"])
        assert bun.get_name() == data.BunData.SPECIAL_CHAR_BUN["name"]

    def test_bun_with_float_price(self):
        bun = Bun(data.BunData.PRECISE_BUN["name"], data.BunData.PRECISE_BUN["price"])
        assert bun.get_price() == data.BunData.PRECISE_BUN["price"]
