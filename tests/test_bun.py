from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun('Зерновая булочка', 255)
        assert bun.get_name() == 'Зерновая булочка'

    def test_bun_get_price(self):
        bun = Bun('Зерновая булочка', 255)
        assert bun.get_price() == 255
