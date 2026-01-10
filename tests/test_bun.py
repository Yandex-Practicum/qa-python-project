from parameterized import parameterized
import unittest
from praktikum.bun import Bun


class TestBunParameterized(unittest.TestCase):

    @parameterized.expand([
        ("Булочка", 50.0),
        ("Черный хлеб", 70.0),
        ("Безглютеновая булочка", 100.0),
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        self.assertEqual(bun.get_name(), name)

    @parameterized.expand([
        ("Булочка", 50.0),
        ("Черный хлеб", 70.0),
        ("Безглютеновая булочка", 100.0),
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        self.assertEqual(bun.get_price(), price)
