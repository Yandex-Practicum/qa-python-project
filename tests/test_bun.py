from praktikum.bun import Bun


class TestBun:

    def test_bun_name(self):
        bun = Bun(name="Classic", price=3.5)
        assert bun.get_name() == "Classic"

    def test_bun_price(self):
        bun = Bun(name="Classic", price=3.5)
        assert bun.get_price() == 3.5
