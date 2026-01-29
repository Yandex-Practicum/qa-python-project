from praktikum.bun import Bun

class TestBun:
    def test_get_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_price(self):
        bun = Bun("white bun", 250)
        assert bun.get_price() == 250
