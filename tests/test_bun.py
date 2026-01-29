import pytest


from info import InfoBun
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [
        (InfoBun.RYE_BUN, 10),
        (InfoBun.CEREAL_BUN, 9),
        (InfoBun.BUN_WITH_POPPY_SEED, 8)
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price(self):
        bun = Bun(InfoBun.BUN_WITH_POPPY_SEED, price=10)
        assert bun.get_price() == 10

    def test_price(self):
        bun = Bun(InfoBun.CEREAL_BUN, price=9)
        bun_1 = Bun(InfoBun.BUN_WITH_POPPY_SEED, price=8)
        assert bun.get_price() and bun_1.get_price() < 10
