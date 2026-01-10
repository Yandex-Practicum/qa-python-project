from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun('Бриошь', 100.0)

        assert bun.get_name() == 'Бриошь'

    def test_get_price(self):
        bun = Bun('Бриошь', 100.0)

        assert bun.get_price() == 100.0
