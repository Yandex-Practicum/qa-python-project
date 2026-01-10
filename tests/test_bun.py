
class TestBun:
    def test_bun_name(self, bun):
        assert bun.get_name() == "Cheese Burger"

    def test_bun_price(self, bun):
        assert bun.get_price() == 10.22
