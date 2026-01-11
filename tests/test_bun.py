import pytest
from praktikum.bun import Bun
from data import BUNS

class TestBun:
    @pytest.mark.parametrize("bun_data", BUNS, ids=[bun["name"] for bun in BUNS])
    def test_get_name(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_name() == bun_data["name"]

    @pytest.mark.parametrize("bun_data", BUNS, ids=[bun["name"] for bun in BUNS])
    def test_get_price(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_price() == bun_data["price"]