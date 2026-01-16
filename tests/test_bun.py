import pytest
from praktikum.praktikum import Bun
from data import TestData
class TestBun:

    @pytest.mark.parametrize('name,price',
                             ((TestData.buns[0][0], TestData.buns[0][1]),
                             (TestData.buns[1][0], TestData.buns[1][1])))
    def test_get_name(self, name, price):
        bun = Bun(name,price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name,price',
                             ((TestData.buns[0][0], TestData.buns[0][1]),
                              (TestData.buns[1][0], TestData.buns[1][1])))
    def test_get_price(self, name, price):
        bun = Bun(name,price)
        assert bun.get_price() == price


