from praktikum.praktikum import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun('Марсианская булочка', 1000)
        assert bun.get_name() == 'Марсианская булочка'

    def test_bun_get_price(self):
        bun = Bun('Марсианская булочка', 1000)
        assert bun.get_price() == 1000
