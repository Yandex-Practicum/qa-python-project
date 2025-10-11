from praktikum.bun import Bun

class TestBun:

    def test_bun_name_get(self):
        bun = Bun("red bun", 150)
        assert bun.get_name() == "red bun"

    def test_bun_price_get(self):
        bun = Bun("black bun", 100)
        assert bun.get_price() == 100