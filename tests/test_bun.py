from bun import Bun
from unittest.mock import Mock

class TestBun:
    def test_get_name_return_set_name(self):
        bun = Bun('Andrey', 2.3)
        assert bun.get_name() == 'Andrey'

    def test_get_price_return_set_price(self):
        bun = Bun('Andrey', 2.3)
        assert bun.get_price() == 2.3

    def test_init(self):
        bun = Bun('Andrey', 2.3)
        assert bun.name == 'Andrey'
        assert bun.price == 2.3
