from bun import Bun

class TestBun:
    def test_init_valid_name_true(self):
        bun = Bun("black bun", 100)
        assert bun.name == "black bun"


    def test_init_valid_price_true(self):
        bun = Bun("black bun", 100)
        assert bun.price == 100

    def test_get_name_valid_bun_returns_name(self):
        bun = Bun("white bun", 50)

        assert bun.get_name() == "white bun"

    def test_get_price_valid_bun_returns_price(self):
        bun = Bun("red bun", 150)
        assert bun.get_price() == 150
