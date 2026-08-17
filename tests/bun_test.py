from praktikum.bun import Bun


class TestBun:
    def setup_method(self):
        self.bun = Bun('Булочка', 100)

    def test_name(self):
        name = self.bun.get_name()
        assert name == 'Булочка'

    def test_price(self):
        price = self.bun.get_price()
        assert price == 100
