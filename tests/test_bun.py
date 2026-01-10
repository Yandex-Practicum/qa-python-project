import pytest

from data import BunTestData
from praktikum.bun import Bun


class TestsBun:
    @pytest.mark.parametrize('td_bun', BunTestData.buns)
    def test_get_bun_name(self, td_bun):
        bun = Bun(td_bun, 5000)
        assert bun.get_name() == td_bun

    @pytest.mark.parametrize('td_price', BunTestData.price)
    def test_get_bun_price(self, td_price):
        bun = Bun('Вcеценовая булка', td_price)
        assert bun.get_price() == td_price