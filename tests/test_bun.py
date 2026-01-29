from praktikum.bun import Bun


class TestBun:
    def test_get_name_name_got(self):
        bun = Bun("Красный гигант", 65.5)
        assert bun.get_name() == "Красный гигант"

    def test_get_price_price_got(self):
        bun = Bun("Красный гигант", 65.5)
        assert bun.get_price() == 65.5
