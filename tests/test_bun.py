class TestBun:

    def test_name_of_bun_true(self, bun):
        assert bun.name == "black bun"

    def test_price_of_bun_true(self, bun):
        assert bun.price == 100

    def test_get_name(self, bun):
        assert bun.get_name() == "black bun"

    def test_get_price(self, bun):
        assert bun.get_price() == 100
