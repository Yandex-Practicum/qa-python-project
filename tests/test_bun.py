from praktikum.bun import Bun

class TestBun:
    def test_bun_creation(self):
        bun = Bun("black bun", 100.0)
        assert bun.name == "black bun"
        assert bun.price == 100.0

    def test_get_name(self):
        bun = Bun("white bun", 200.0)
        assert bun.get_name() == "white bun"

    def test_get_price(self):
        bun = Bun("red bun", 300.0)
        assert bun.get_price() == 300.0