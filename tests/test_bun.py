import pytest

from bun import Bun
from helpers.data import BUNS_INFO

class TestBun:

    @pytest.mark.parametrize("bun_data", BUNS_INFO)
    def test_get_name_returns_bun_name(self, bun_data):
        bun = Bun(bun_data["bun_name"], bun_data["bun_price"])

        assert bun.get_name() == bun_data["bun_name"]
        assert isinstance(bun_data["bun_name"], str)

    @pytest.mark.parametrize("bun_data", BUNS_INFO)
    def test_get_price_returns_bun_price(self, bun_data):
        bun = Bun(bun_data["bun_name"], bun_data["bun_price"])

        assert bun.get_price() == bun_data["bun_price"]
        assert isinstance(bun_data["bun_price"] , float)