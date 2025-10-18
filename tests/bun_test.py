import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBun:

    def test_get_name_returns_correct_name(self):
        bun = Bun("Краторная булка", 100.0)
        assert bun.get_name() == "Краторная булка"

    def test_get_price_returns_correct_price(self):
        bun = Bun("Флюоресцентная булка", 200.0)
        assert bun.get_price() == 200.0

    def test_bun_with_zero_price(self):
        bun = Bun("Бесплатная булка", 0.0)
        assert bun.get_price() == 0.0

    def test_bun_with_special_characters_in_name(self):
        bun = Bun("Булка с №1", 150.0)
        assert bun.get_name() == "Булка с №1"

    def test_bun_with_float_price(self):
        bun = Bun("Точная булка", 99.99)
        assert bun.get_price() == 99.99
