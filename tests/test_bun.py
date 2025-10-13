from praktikum.bun import Bun


class TestBun:
    def test_get_name_returns_correct_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_price_returns_correct_price(self):
        bun = Bun("white bun", 200)
        assert bun.get_price() == 200
