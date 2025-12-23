
class TestBun:

    def test_get_name(self, default_bun):
        bun_name, _ = default_bun.get_name(), default_bun.get_price()
        assert default_bun.get_name() == bun_name

    def test_get_price(self, default_bun):
        _, bun_price = default_bun.get_name(), default_bun.get_price()
        assert default_bun.get_price() == bun_price
