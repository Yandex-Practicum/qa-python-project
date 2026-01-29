class TestBun:

    def test_get_name(self, bun):
        assert bun.get_name() is bun.name

    def test_get_price(self, bun):
        assert bun.get_price() is bun.price
