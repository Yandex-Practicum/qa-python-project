from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun('bun_name', 100.0)

        assert bun.get_name() == 'bun_name'

    def test_get_price(self):
        bun = Bun('bun_name', 100.0)

        assert bun.get_price() == 100.0
