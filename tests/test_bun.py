

class TestBun:

    def test_bun_constructor(self, create_bun):
        assert isinstance(create_bun.name, str) and isinstance(create_bun.price, float)

    def test_get_bun_name(self, create_bun):
        assert create_bun.get_name() == create_bun.name

    def test_get_bun_price(self, create_bun):
        assert create_bun.get_price() == create_bun.price
