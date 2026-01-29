import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name_expected', ['small green bun', ''])
    def test_get_name(self, name_expected):
        bun = Bun(name_expected, 100.001)
        name_extracted = bun.get_name()

        assert name_expected == name_extracted

    @pytest.mark.parametrize('price_expected', [10.02, ''])
    def test_get_price(self, price_expected):
        bun = Bun('test bun', price_expected)
        price_extracted = bun.get_price()

        assert price_expected == price_extracted