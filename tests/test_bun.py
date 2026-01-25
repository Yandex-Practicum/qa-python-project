from praktikum.bun import Bun


class TestBun:
    def test_get_name(self):
        bun = Bun('Hleb', 2)
        assert bun.get_name() == 'Hleb'

    def test_get_price(self):
        bun = Bun('NeHleb', 2)
        assert bun.get_price() == 2
