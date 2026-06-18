class TestBun:

    def test_getting_name(self, bun):
        assert bun.get_name() == "black bun"

    def test_getting_price(self, bun):
        assert bun.get_price() == 100.0
