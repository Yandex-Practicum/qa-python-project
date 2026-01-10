import pytest

from bun import Bun
from data import Data


class TestBun:

    @pytest.mark.parametrize('name, price',
                             ((Data.bulka_1[0], Data.bulka_1[1]),
                              (Data.bulka_2[0], Data.bulka_2[1])))
    def test_get_name_and_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price',
                             ((Data.bulka_1[0], Data.bulka_1[1]),
                              (Data.bulka_2[0], Data.bulka_2[1])))
    def test_get_name_and_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price











