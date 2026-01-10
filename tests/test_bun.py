from praktikum.bun import Bun
from data import TestData

class TestBun:

    def test_get_bun_name(self):

        bun = Bun(TestData.bun_names[0], TestData.prices[0])

        assert bun.get_name() == TestData.bun_names[0]

    def test_get_bun_price(self):

        bun = Bun(TestData.bun_names[1], TestData.prices[1])

        assert bun.get_price() == TestData.prices[1]