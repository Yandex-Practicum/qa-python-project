import pytest
from praktikum.praktikum import Bun


class TestBun:

    @pytest.mark.parametrize("name_bun", ["Флюоресцентная булка", "Краторная булка", "Bun"])
    def test_get_name_bun(self, name_bun):
        bun = Bun(name_bun, 99.9)
        assert bun.get_name() == name_bun

    @pytest.mark.parametrize("price_bun", [99.9, 100, 1000000.1, 1.000001])
    def test_get_price_bun(self, price_bun):
        bun = Bun("Bun", price_bun)
        assert bun.get_price() == price_bun
