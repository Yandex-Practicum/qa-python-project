import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name", ["Булка 1", "", "Необычная булка"])
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, 500)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [1000.5, 0, -50])
    def test_get_price_returns_correct_price(self, price):
        bun = Bun("Необычная булка", price)
        assert bun.get_price() == price
