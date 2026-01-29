from praktikum.bun import Bun


class TestBun:

    def test_get_bun_name(self):
        bun = Bun('Лембас', 25)
        bun_name = bun.get_name()
        assert bun_name == 'Лембас'

    def test_get_bun_price(self):
        bun = Bun('Лембас', 25)
        bun_price = bun.get_price()
        assert bun_price == 25
