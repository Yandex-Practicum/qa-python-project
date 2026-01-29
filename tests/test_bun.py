class TestBun:
    def test_bun_name_price(self, bun):
        name = bun.name
        price = bun.price
        assert bun.get_name() == name
        assert bun.get_price() == price
