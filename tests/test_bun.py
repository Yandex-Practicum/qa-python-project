from praktikum.bun import Bun


class TestBun:

    def test_get_name_with_exist_bun_returns_bun_name(self):
        bun = Bun("white bun", 200)

        assert bun.get_name() == "white bun"

    def test_get_price_with_exist_bun_returns_bun_price(self):
        bun = Bun("red bun", 300)

        assert bun.get_price() == 300