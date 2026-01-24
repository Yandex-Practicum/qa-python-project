from praktikum.bun import Bun


class TestBun:

    def test_bun_get_name(self):
        bun = Bun("Black bun", 100)
        assert bun.get_name() == "Black bun"

    def test_bun_get_price(self):
        bun = Bun("Black bun", 100)
        assert bun.get_price() == 100

