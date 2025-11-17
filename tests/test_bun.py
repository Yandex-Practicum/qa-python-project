from praktikum.bun import Bun

class TestBun:

    def test_get_name(self):
        bun = Bun('Булка', 100)
        assert bun.get_name() == 'Булка'

    def test_get_price(self):
        bun = Bun('Булка', 100)
        assert bun.get_price() == 100