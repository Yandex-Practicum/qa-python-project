class TestBun:
    def test_bun_properties_match_methods(self, bun):
            assert bun.get_name() == bun.name
            assert bun.get_price() == bun.price

    def test_bun_name(self, bun):
            assert bun.name == "black bun"
            assert bun.get_name() == "black bun"

    def test_bun_price(self, bun):
            assert bun.price == 100
            assert bun.get_price() == 100