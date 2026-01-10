class TestBun:
    def test_name_matches_expected(self, test_bun):
        assert test_bun.get_name() == "Kratorskaya"

    def test_name_is_string(self, test_bun):
        assert isinstance(test_bun.get_name(), str)

    def test_price_matches_expected(self, test_bun):
        assert test_bun.get_price() == 1255

    def test_price_is_int(self, test_bun):
        assert isinstance(test_bun.get_price(), int)
