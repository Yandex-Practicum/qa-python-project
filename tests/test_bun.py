import unittest
from praktikum.bun import Bun
from data import Burger1


class TestBun(unittest.TestCase):

    def test_name_of_bun_init(self):
        bun = Bun(Burger1().bun_name, Burger1().bun_price)
        assert bun.name == 'Краторная булка N-200i' and type(bun.name) == str

    def test_price_of_bun_init(self):
        bun = Bun(Burger1().bun_name, Burger1().bun_price)
        assert bun.price == 1255.0 and type(bun.price) == float

    def test_get_name(self):
        bun = Bun(Burger1().bun_name, Burger1().bun_price)
        bun.get_name()
        assert bun.get_name() == 'Краторная булка N-200i' and type(bun.get_name()) == str

    def test_get_price(self):
        bun = Bun(Burger1().bun_name, Burger1().bun_price)
        bun.get_price()
        assert bun.get_price() == 1255.0 and type(bun.get_price()) == float
