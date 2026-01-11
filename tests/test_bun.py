from bun import Bun


class TestBun:

    def test_init_name(self):
        bun = Bun("Кокосовая", 100)
        assert bun.name == "Кокосовая"

    def test_init_price(self):
        bun = Bun("Кокосовая", 100)
        assert bun.price == 100

    def test_get_name(self):
        bun = Bun("Кокосовая", 100)
        assert bun.get_name() == "Кокосовая"

    def test_get_price(self):
        bun = Bun("Кокосовая", 100)
        assert bun.get_price() == 100
