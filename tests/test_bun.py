import unittest
from praktikum.praktikum import Bun

class TestBun(unittest.TestCase):

    def setUp(self):
        self.bun = Bun('Sesame', 50.0)

    def test_bun_name(self):
        self.assertEqual(self.bun.name, 'Sesame')

    def test_bun_price(self):
        self.assertEqual(self.bun.price, 50.0)

    def test_get_name(self):
        self.assertEqual(self.bun.get_name(), 'Sesame')

    def test_get_price(self):
        self.assertEqual(self.bun.get_price(), 50.0)

if __name__ == '__main__':
    unittest.main()
